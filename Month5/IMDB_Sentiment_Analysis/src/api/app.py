from fastapi import FastAPI
from src.api.schemas import ReviewRequest, PredictionResponse
from src.inference.predict import predict_sentiment

app = FastAPI(
title="IMDb Sentiment Analysis API",
description="LSTM-based Movie Review Sentiment Analysis",
version="1.0.0"
)

@app.get("/")
def home():
    return {
"message": "IMDb Sentiment Analysis API is running"
}

@app.get("/health")
def health():
    return {
"status": "healthy"
}

@app.post(
"/predict",
response_model=PredictionResponse
)
def predict(request: ReviewRequest):
    result = predict_sentiment(
    request.review
)
    return PredictionResponse(
    sentiment=result["sentiment"],
    confidence=result["confidence"]
)

