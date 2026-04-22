FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["waitress-serve", "--listen=0.0.0.0:8080", "main:app"]