
# 🏡 House Price Prediction using Machine Learning

A complete **end-to-end Machine Learning project** that predicts house prices based on various features such as area, number of rooms, location, and property type.

This project demonstrates a **full ML pipeline**, including data preprocessing, model training, evaluation, visualization, and optional deployment using Flask.

---

# 📌 Project Description

House price prediction is a crucial problem in real estate analytics. Accurate estimation helps buyers, sellers, and investors make informed decisions.

### ❗ Problem Statement
Determining the correct price of a house manually is challenging due to multiple influencing factors like location, size, and amenities.

### 🎯 Solution
This project uses **machine learning regression models** to predict house prices based on historical data, improving accuracy and efficiency.

---

# 🚀 Features

- ✅ End-to-end ML pipeline  
- 📊 Data preprocessing & feature engineering  
- 🤖 Multiple regression models  
- 📈 Model comparison  
- 🔥 Feature importance visualization  
- 📉 Actual vs Predicted price plots  
- 🌐 Flask web app for predictions (optional)  

---

# 🧰 Tech Stack

- **Language:** Python 🐍  
- **Libraries:**
  - Pandas, NumPy  
  - Scikit-learn  
  - Matplotlib, Seaborn  
- **Framework:** Flask (for deployment)  

---

# 📊 Dataset Description

The dataset contains features such as:

| Feature | Description |
|--------|------------|
| Area | Size of the property (sq ft) |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Location | Area type (City Center, Suburb, Rural) |
| Property_Type | Apartment / House / Villa |
| Age | Age of the property |
| Price | Target variable (house price) |

### 🎯 Target Variable:
- **Price** → Continuous value (Regression problem)

---

# 📁 Project Structure

```bash
house_price_prediction/
│
├── data/
│   └── house_prices.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_inference.py
│   └── web_app.py          # Flask app (optional)
│
├── models/
│   ├── *.pkl
│   └── plots/
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md
