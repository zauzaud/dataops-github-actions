FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY conecta_postgres.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "4", "app:app"]
