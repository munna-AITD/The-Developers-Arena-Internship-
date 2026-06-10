# API Documentation

## Base URL

http://localhost:8000

---

## Health Check

GET /health

Response:

{
    "status": "healthy"
}

---

## Predict Sentiment

POST /predict

Request:

{
    "review": "This movie was amazing."
}

Response:

{
    "sentiment": "Positive",
    "confidence": 0.95
}

---

## Swagger UI

http://localhost:8000/docs