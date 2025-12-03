# build
FROM alpine AS builder 

WORKDIR /app
COPY index.html . 
COPY nginx.conf /etc/nginx/nginx.conf

# runtime
FROM nginx:alpine

COPY --from=builder /app/index.html /usr/share/nginx/html/index.html
COPY --from=builder /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# lancer
CMD ["nginx", "-g", "daemon off;"]