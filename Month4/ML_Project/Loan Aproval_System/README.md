# 🏦 Loan Approval Prediction System using Machine Learning

A complete **end-to-end Machine Learning project** that predicts whether a loan application will be **Approved ✅ or Rejected ❌** based on applicant financial and personal details.

This project demonstrates a **production-ready ML pipeline** with model training, evaluation, visualization, and deployment via both a **Flask web interface** and a **REST API**.

---

# 📌 Problem Statement

Loan approval in financial institutions is traditionally a **manual and time-consuming process** that may involve:

- Human bias  
- Inconsistent decision-making  
- High processing time  
- Difficulty handling large-scale applications  

👉 This project solves the problem by building an **automated, data-driven system** that predicts loan approval efficiently and accurately.

---

# 🚀 Features

- ✅ End-to-end ML pipeline  
- 🤖 Multiple model training & comparison  
- ⚙️ Data preprocessing using `ColumnTransformer`  
- 📊 Model evaluation (Accuracy, Confusion Matrix, Classification Report)  
- 🔥 Feature importance visualization  
- 🌐 Flask-based Web UI  
- 🔌 REST API for model serving (`api.py`)  
- ⚙️ Config-based modular architecture (`config.py`)  
- 📁 Clean and scalable project structure  

---

# 🧰 Tech Stack

- **Language:** Python 🐍  
- **Libraries:**
  - Pandas, NumPy  
  - Scikit-learn  
  - Matplotlib, Seaborn  
- **Framework:** Flask  
- **Tools:** Joblib, JSON, REST API  

---

# 📁 Project Structure

```bash
loan_approval_system/
│
├── data/                     # Dataset
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_inference.py
│   ├── web_app.py           # Flask UI
│   └── api.py               # REST API
│
├── models/                  # Saved models & outputs
│   ├── *.pkl
│   ├── *_confusion_matrix.png
│   ├── *_feature_importance.png
│   └── *_classification_report.csv
│
├── templates/               # HTML files
│   └── index.html
│
├── config/
│   └── config.py            # Configuration settings
│
├── requirements.txt
└── README.md
