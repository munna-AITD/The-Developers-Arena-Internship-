from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Embedding,
    Bidirectional,
    LSTM,
    Dense,
    Dropout,
    Input
)


def build_lstm_model(
        vocab_size,
        embedding_dim,
        max_length):

    model = Sequential([

        Input(
            shape=(max_length,)
        ),

        Embedding(
            input_dim=vocab_size,
            output_dim=embedding_dim
        ),

        Bidirectional(LSTM(128)),

        Dropout(0.5),
        
        Dense(32,activation="relu"),
        Dropout(0.2),

        Dense(1,activation="sigmoid")])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model