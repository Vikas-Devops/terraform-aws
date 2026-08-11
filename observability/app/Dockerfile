FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["opentelemetry-instrument", \
     "--service_name", "sre-demo-service", \
     "--traces_exporter", "otlp", \
     "--metrics_exporter", "otlp", \
     "--exporter_otlp_endpoint", "http://otel-collector:4317", \
     "gunicorn", \
     "--bind", "0.0.0.0:8080", \
     "app:app"]