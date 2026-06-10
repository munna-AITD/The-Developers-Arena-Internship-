import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.callbacks import EarlyStopping

from src.models.lstm_model import build_lstm_model


# Configuration
MAX_WORDS = 10000
MAX_LENGTH = 100
EMBEDDING_DIM = 64
BATCH_SIZE = 32
EPOCHS = 10


# Load Dataset
print("Loading dataset...")

df = pd.read_csv(
    "data/processed/imdb_cleaned.csv"
)
df["sentiment"] = df["sentiment"].map({
    "negative": 0,
    "positive": 1
})
X = df["clean_review"]
y = df["sentiment"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train Size:", len(X_train))
print("Test Size:", len(X_test))


# Tokenization
tokenizer = Tokenizer(
    num_words=MAX_WORDS,
    oov_token="<OOV>"
)

tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(
    X_train
)

X_test_seq = tokenizer.texts_to_sequences(
    X_test
)

# Padding
X_train_pad = pad_sequences(
    X_train_seq,
    maxlen=MAX_LENGTH,
    padding="post",
    truncating="post"
)

X_test_pad = pad_sequences(
    X_test_seq,
    maxlen=MAX_LENGTH,
    padding="post",
    truncating="post"
)


# Build Model
vocab_size = min(
    MAX_WORDS,
    len(tokenizer.word_index) + 1
)

model = build_lstm_model(
    vocab_size=vocab_size,
    embedding_dim=EMBEDDING_DIM,
    max_length=MAX_LENGTH
)

model.summary()


# Early Stopping
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=2,
    restore_best_weights=True
)


# Training
history = model.fit(
    X_train_pad,
    y_train,
    validation_split=0.2,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    callbacks=[early_stop]
)
from src.monitoring.visualization import (
    plot_training_history
)

plot_training_history(history)
# Evaluation
loss, accuracy = model.evaluate(
    X_test_pad,
    y_test
)

print(f"\nTest Accuracy: {accuracy:.4f}")
from sklearn.metrics import (
    classification_report
)

from src.monitoring.metrics import (
    calculate_metrics,
    generate_report
)

pred_prob = model.predict(
    X_test_pad
)

y_pred = (
    pred_prob > 0.5
).astype(int)

metrics = calculate_metrics(
    y_test,
    y_pred
)

print(metrics)

generate_report(
    y_test,
    y_pred
)
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from src.monitoring.model_monitor import save_metrics

# Predictions
y_pred_prob = model.predict(X_test_pad)

y_pred = (y_pred_prob > 0.5).astype(int)

# Metrics dictionary
metrics = {
    "accuracy": accuracy_score(y_test, y_pred),
    "precision": precision_score(y_test, y_pred),
    "recall": recall_score(y_test, y_pred),
    "f1_score": f1_score(y_test, y_pred)
}

print(metrics)

# Save metrics
save_metrics(metrics)


# Save Model
model.save(
    "models/imdb_lstm.keras"
)

print("Model Saved")


# Save Tokenizer
with open(
    "models/tokenizer.pkl",
    "wb"
) as f:

    pickle.dump(
        tokenizer,
        f
    )

print("Tokenizer Saved")