from src.inference.predict import predict_sentiment

def test_positive_review():
    result = predict_sentiment(
    "This movie was fantastic and wonderful.")
    assert "sentiment" in result
    assert "confidence" in result

def test_negative_review():
    result = predict_sentiment(
    "This movie was terrible and boring."
    )
    assert "sentiment" in result
    assert "confidence" in result
