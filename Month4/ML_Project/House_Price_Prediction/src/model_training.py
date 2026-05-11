from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import joblib
import numpy as np
import pandas as pd
from data_preprocessing import process_data
# Load Process Data
X, y, processor= process_data("C:/Users/Lenovo/Desktop/ml_project/data/house_prices.csv")
# Split the data into training and testing
X_train, X_test, y_train, y_test= train_test_split(X,y, test_size = 0.2, random_state=42)

#Model
rf_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

rf_model.fit(X_train, y_train)

#prediction
y_pred= rf_model.predict(X_test)
# Actual vs Predicted Plot
plt.figure(figsize=(6,6))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")

# Perfect line
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         linestyle='--')

plt.grid(True)
plt.show()
# =====================================================
# 🔥 FEATURE IMPORTANCE
# =====================================================
importance = rf_model.feature_importances_

imp_df = pd.DataFrame({
    "feature": X.columns,
    "importance": importance
}).sort_values(by="importance", ascending=False)

print("\nFeature Importance:\n", imp_df)

# Plot Feature Importance
plt.figure(figsize=(8,5))
plt.barh(imp_df["feature"], imp_df["importance"])
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importance")
plt.gca().invert_yaxis()

plt.savefig("feature_importance.png")  # ✅ Save image
plt.show()
# Save feature importance (optional)
imp_df.to_csv("C:/Users/Lenovo/Desktop/ml_project/models/feature_importance.csv", index=False)

# =====================================================
# 🚀 CROSS VALIDATION
# =====================================================
cv_scores = cross_val_score(rf_model, X, y, cv=5, scoring='r2')

print("\nCross Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())
#Evaluation
print("Train R2:", rf_model.score(X_train, y_train))
print("Test R2:", rf_model.score(X_test, y_test))
print("R2 Score", r2_score(y_test,y_pred))
print("RMSE of the model", np.sqrt(mean_squared_error(y_pred,y_test)))
print(X.columns)

# Save model
joblib.dump(rf_model, "C:/Users/Lenovo/Desktop/ml_project/models/model.pkl")
joblib.dump(processor, "C:/Users/Lenovo/Desktop/ml_project/models/preprocessor.pkl")