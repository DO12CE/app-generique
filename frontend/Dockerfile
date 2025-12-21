# Dockerfile multi étapes pour le front et configuration Nginx avec reverse proxy (3b)
FROM alpine AS builder 

WORKDIR /app
COPY index.html . 
COPY nginx.conf /etc/nginx/nginx.conf

FROM nginx:alpine

COPY --from=builder /app/index.html /usr/share/nginx/html/index.html
COPY --from=builder /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# pour ne pas être en root (1c/5a)
USER appuser


CMD ["nginx", "-g", "daemon off;"]