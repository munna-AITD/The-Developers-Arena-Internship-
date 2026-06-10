import pickle
import re
import string

from bs4 import BeautifulSoup

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Configuration
MAX_LENGTH = 100

# Load Model
model = load_model("models/imdb_lstm.keras")

# Load Tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


def clean_text(text):
    """
    Text preprocessing
    """

    text = str(text)

    text = BeautifulSoup(
        text,
        "html.parser"
    ).get_text()

    text = text.lower()

    text = re.sub(
        r"http\S+|www\S+|https\S+",
        "",
        text
    )

    text = re.sub(
        r"\d+",
        "",
        text
    )

    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def predict_sentiment(review):

    # Clean review
    review = clean_text(review)

    # Convert to sequence
    sequence = tokenizer.texts_to_sequences(
        [review]
    )

    # Padding
    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    # Prediction
    probability = model.predict(
        padded,
        verbose=0
    )[0][0]

    # Binary Classification
    if probability >= 0.5:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return {
        "review": review,
        "sentiment": sentiment,
        "confidence": float(probability)
    }


if __name__ == "__main__":

    sample_review = """
    This movie was absolutely amazing.
    The acting was fantastic and
    the story was brilliant.
    """

    result = predict_sentiment(
        sample_review
    )

    print("\nPrediction Result")
    print(result)