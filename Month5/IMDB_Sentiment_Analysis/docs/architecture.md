# Project Architecture

## Overview

The IMDb Sentiment Analysis system follows a modular machine learning architecture.

Data Flow:

Raw Data
    ↓
Data Preprocessing
    ↓
Tokenization
    ↓
Sequence Padding
    ↓
LSTM Model
    ↓
Prediction Layer
    ↓
FastAPI Service
    ↓
User/API Consumer

## Components

### Data Processing
Responsible for:
- Text Cleaning
- Stopword Removal
- Tokenization
- Sequence Creation

### Model Training
Responsible for:
- Data Splitting
- Model Training
- Evaluation
- Model Persistence

### Inference
Responsible for:
- Loading Trained Model
- Text Processing
- Prediction Generation

### Monitoring
Responsible for:
- Metrics Tracking
- Logging
- Visualization

### API
Responsible for:
- REST Endpoints
- Prediction Requests
- Health Monitoring