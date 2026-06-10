# Model Documentation

## Model Type

Bidirectional LSTM

## Architecture

Embedding Layer

↓

Bidirectional LSTM (64)

↓

Dropout (0.5)

↓

Bidirectional LSTM (32)

↓

Dropout (0.3)

↓

Dense (24)

↓

Softmax Output Layer

## Hyperparameters

Embedding Dimension: 64

Max Vocabulary Size: 10000

Max Sequence Length: 100

Batch Size: 32

Epochs: 10

Optimizer: Adam

Loss Function:
Sparse Categorical Crossentropy

## Performance

Training Accuracy: 93%

Validation Accuracy: 86%

Test Accuracy: 83%