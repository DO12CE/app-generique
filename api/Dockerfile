# Builder
# 
FROM python:3.11-slim AS builder 

WORKDIR /app
COPY requirements.txt .
# cache layer
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Runtime
FROM python:3.11-slim

RUN adduser --system --uid 1000 appuser

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /app /app

EXPOSE 8080

USER appuser

# lancement
CMD ["python", "app.py"]