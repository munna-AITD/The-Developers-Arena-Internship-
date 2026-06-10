# IMDb Sentiment Analysis using Deep Learning (LSTM)

## Project Overview

This project performs sentiment analysis on IMDb movie reviews using a Bidirectional LSTM deep learning model. The system classifies reviews into sentiment categories based on textual content and exposes predictions through a FastAPI REST API.

The project follows a production-ready machine learning workflow including:

* Data preprocessing
* Model training
* Model evaluation
* Inference pipeline
* API deployment
* Monitoring and visualization
* Docker support
* Cloud deployment configuration

---

## Problem Statement

Movie reviews contain valuable information about customer opinions. Manually analyzing thousands of reviews is time-consuming.

The objective of this project is to build a deep learning model capable of automatically predicting the sentiment of movie reviews.

---

## Dataset

Dataset: IMDb Movie Reviews Dataset

Features:

* Review Text
* Sentiment Label

Sentiment Classes:

* Positive
* Negative

---

## Project Structure

```text
Imdb_Sentiment_Analysis/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data_processing/
│   ├── models/
│   ├── training/
│   ├── inference/
│   ├── api/
│   └── monitoring/
│
├── models/
│   ├── imdb_lstm.keras
│   └── tokenizer.pkl
│
├── reports/
│   ├── figures/
│   └── metrics/
│
├── deployment/
├── docker/
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Data Preprocessing

The following preprocessing steps were performed:

* Lowercasing
* HTML tag removal
* Special character removal
* Stopword removal
* Tokenization
* Sequence Padding

TensorFlow Tokenizer was used to convert text into numerical sequences.

---

## Model Architecture

Model Type:

Bidirectional LSTM

Architecture:

Embedding Layer

↓

Bidirectional LSTM (64 units)

↓

Dropout (0.5)

↓

Bidirectional LSTM (32 units)

↓

Dropout (0.3)

↓

Dense Layer (24 units)

↓

Output Layer (Softmax)

---

## Training Configuration

| Parameter      | Value                           |
| -------------- | ------------------------------- |
| Optimizer      | Adam                            |
| Loss Function  | Sparse Categorical Crossentropy |
| Batch Size     | 32                              |
| Epochs         | 10                              |
| Early Stopping | Enabled                         |

---

## Model Performance

Performance obtained during experimentation:

| Metric              | Score |
| ------------------- | ----- |
| Training Accuracy   | 93%   |
| Validation Accuracy | 86%   |
| Test Accuracy       | 83%   |

The model demonstrates strong generalization performance with minimal overfitting.

---

## Monitoring and Visualization

Generated Artifacts:

* Accuracy Curve
* Loss Curve
* Classification Report
* Confusion Matrix
* Evaluation Metrics

Stored in:

```text
reports/
```

---

## FastAPI REST API

Start API:

```bash
uvicorn src.api.app:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Health Check:

```text
GET /health
```

Prediction Endpoint:

```text
POST /predict
```

Example Request:

```json
{
  "review": "This movie was absolutely fantastic."
}
```

Example Response:

```json
{
  "sentiment": "Positive",
  "confidence": 0.95
}
```

---

## Installation

Clone Repository

```bash
git clone <repository-url>
```

Move into Project Directory

```bash
cd Imdb_Sentiment_Analysis
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Model Training

Run:

```bash
python -m src.training.train
```

---

## Data Preparation

Run:

```bash
python -m src.data_processing.prepare_data
```

---

## Inference

Run:

```bash
python -m src.inference.predict
```

---

## Docker

Build Image

```bash
docker build -f docker/Dockerfile -t imdb-sentiment-api .
```

Run Container

```bash
docker run -p 8000:8000 imdb-sentiment-api
```

---

## Future Improvements

* Transformer-based Models (BERT)
* Attention Mechanisms
* Model Monitoring Dashboard
* CI/CD Pipeline
* Cloud Deployment
* Explainable AI (SHAP/LIME)

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Scikit-Learn
* NLTK
* FastAPI
* Matplotlib
* Docker
## Testing

Run all tests:

```bash
python -m pytest tests/
```

Test Results:

```text
5 passed
```

Covered Components:

* API Endpoints
* Health Checks
* Model Inference
* Data Preprocessing
* Integration Validation

```
```

---

## Author

Munna Kumar

PhD Research Scholar

Machine Learning | Deep Learning | Data Science
