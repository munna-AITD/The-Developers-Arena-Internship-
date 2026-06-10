from src.data_processing.preprocess import clean_text

def test_clean_text():

    text = "<html>Hello!!! This is a TEST.</html>"

    cleaned = clean_text(text)

    assert isinstance(cleaned, str)
    assert len(cleaned) > 0