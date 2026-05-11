from src.model_inference import predict

def test_prediction():
    result = predict([1200, 3, 2, 35,"Rural","House"])
    assert result > 0