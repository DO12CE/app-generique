# Dockerfile multi étapes pour le front et configuration Nginx avec reverse proxy (3b)
FROM alpine AS builder 

WORKDIR /app
COPY index.html . 
COPY nginx.conf /etc/nginx/nginx.conf

FROM nginx:alpine

# utilisateur non root (5a) 
RUN adduser -D -u 1000 appuser

# On donne les droits à l'utilisateur sur les dossiers Nginx
RUN touch /var/run/nginx.pid && \
chown -R appuser:appuser /usr/share/nginx/html /var/cache/nginx /var/run /var/log/nginx

WORKDIR /usr/share/nginx/html

COPY --from=builder /app/index.html .
COPY --from=builder /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf


# pour ne pas être en root (1c/5a)
USER appuser

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]