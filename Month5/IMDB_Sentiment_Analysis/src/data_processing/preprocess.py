import re
import string
import pandas as pd
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (first run only)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    """
    Complete text preprocessing pipeline
    """

    # Convert to string
    text = str(text)

    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Tokenization
    words = text.split()

    # Remove stopwords
    words = [
        word for word in words
        if word not in stop_words
    ]

    # Lemmatization
    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    # Join back
    text = ' '.join(words)

    return text.strip()


def encode_sentiment(sentiment):
    """
    Convert labels to numeric values
    """

    sentiment_map = {
        'negative': 0,
        'positive': 1
    }

    return sentiment_map[sentiment]


if __name__ == "__main__":

    sample_text = """
    <html>
    This movie was AMAZING!!!
    I watched it 3 times.
    Visit https://example.com
    </html>
    """

    print(clean_text(sample_text))