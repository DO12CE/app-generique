========================================================================
PROJET : APPLICATION 3-TIER CONTENEURISÉE
AUTEUR : Yousra Zaabat
DATE   : 21/12/2025
CONTEXTE : Module DOCKER (B3DEVIA)
========================================================================

1. DESCRIPTION DU PROJET
------------------------------------------------------------------------
Ce projet met en œuvre une architecture web complète (Frontend, Backend, 
Base de données) entièrement conteneurisée et orchestrée avec Docker Compose.

L'architecture repose sur 3 tiers :
1. Frontend : Serveur Nginx (Alpine) servant l'interface et agissant 
   [cite_start]comme Reverse-Proxy [cite: 127-131].
2. [cite_start]Backend  : API Python Flask exposant les routes /status et /items [cite: 56-59].
3. [cite_start]Database : PostgreSQL 16 (Alpine) avec persistance des données[cite: 13].

2. FONCTIONNALITÉS CLÉS ET SÉCURITÉ
------------------------------------------------------------------------
- [cite_start]Builds Multi-étapes : Réduction de la taille des images (API & Front)[cite: 326].
- [cite_start]Sécurité Non-Root : Utilisation d'un utilisateur 'appuser' limité[cite: 343].
- [cite_start]Images Légères : Utilisation exclusive de bases Alpine et Slim[cite: 331].
- [cite_start]Automatisation : Script de déploiement (Validation, Build, Scan, Run)[cite: 268].
- [cite_start]Healthchecks : Gestion automatique de l'ordre de démarrage[cite: 210].
- [cite_start]Configuration : Externalisation des variables sensibles (.env)[cite: 87].

3. PRÉREQUIS
------------------------------------------------------------------------
- Docker Desktop ou Docker Engine
- Docker Compose
- Un terminal (Bash, PowerShell, ou Git Bash)

4. INSTALLATION ET DÉMARRAGE RAPIDE (PIPELINE)
------------------------------------------------------------------------
Un script d'automatisation est fourni pour simplifier le cycle de vie.
Il simule une pipeline CI/CD locale en exécutant les étapes suivantes :

    1. Config : Vérification du fichier docker-compose.yml.
    2. Build  : Construction des images sans cache.
    3. Scout  : Scan de sécurité des vulnérabilités (CVEs).
    4. Trust  : Activation de la signature des images.
    5. Deploy : Lancement des conteneurs.

COMMANDES :
   
   # 1. Rendre le script exécutable (si nécessaire)
   chmod +x scripts/build_and_deploy.sh

   # 2. Lancer la pipeline complète
   ./scripts/build_and_deploy.sh

5. DÉMARRAGE MANUEL (ALTERNATIVE)
------------------------------------------------------------------------
Si vous ne souhaitez pas utiliser le script, vous pouvez lancer :

   docker compose config
   docker compose up -d --build

6. CONFIGURATION (.env)
------------------------------------------------------------------------
Assurez-vous que le fichier .env est présent à la racine avec ce contenu :

   # Base de données
   POSTGRES_USER=app_user_db
   POSTGRES_PASSWORD=password
   POSTGRES_DB=generic_app_db
   DB_HOST=db
   DB_PORT=5432

   # API
   API_PORT=8080
   HOST_API_PORT=8081

   # Frontend
   FRONT_PORT=80
   HOST_FRONT_PORT=80
   API_BASE_URL=http://api:8080

7. ACCÈS ET VÉRIFICATION
------------------------------------------------------------------------
Une fois déployé, vérifiez que les services sont "healthy" :
   
   Commande : docker compose ps

ACCÈS :
- Frontend (Interface) : http://localhost:80
- API (Status)         : http://localhost:8081/status
- API (Données JSON)   : http://localhost:8081/items

8. STRUCTURE DU DOSSIER
------------------------------------------------------------------------
.
|-- api/                # Code source Python et Dockerfile API
|-- frontend/           # Code source HTML/Nginx et Dockerfile Front
|-- db-init/            # Script SQL d'initialisation (init.sql)
|-- scripts/            # Script d'automatisation (build_and_deploy.sh)
|-- docker-compose.yml  # Orchestration des services
|-- .env                # Variables d'environnement
`-- README.txt          # Ce fichier