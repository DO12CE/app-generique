#!/bin/bash
set -e # Arrêt du script si une commande échoue

echo "--- étape 1 - Vérification de la configuration ---"
docker compose config 

echo "--- étape 2 - Construction des images optimisées ---"
docker compose build --no-cache

echo "--- étape 3 - Scan de sécurité (Docker Scout) ---"
docker scout quickview app-generique-api
docker scout quickview app-generique-frontend

echo "--- étape 4 - Signature et Publication ---"
# empêche Docker de pousser ou de tirer des images non signées (5b)
export DOCKER_CONTENT_TRUST=1
# Remplacer par votre utilisateur Docker Hub réel
# docker push [VOTRE_USER]/app-generique-api:latest

echo "--- 5. Déploiement opérationnel ---"
docker compose up -d

echo "Application déployée avec succès !"

