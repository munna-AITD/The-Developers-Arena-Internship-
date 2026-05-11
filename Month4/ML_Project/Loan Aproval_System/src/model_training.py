import os
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config.config import DATA_PATH, MODEL_DIR, RANDOM_STATE, TEST_SIZE
from config.config import PREPROCESSOR_PATH
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

from src.data_preprocessing import process_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

X, y, preprocessor = process_data(DATA_PATH)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
)

models = {
    "random_forest": RandomForestClassifier(n_estimators=200, random_state=42),
    "decision_tree": DecisionTreeClassifier(),
    "logistic_regression": LogisticRegression(max_iter=1000)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_pred)
    cv = cross_val_score(model, X, y, cv=5, scoring='accuracy').mean()

    
    # ================================
    # CLASSIFICATION REPORT (SAVE)
    # ================================
    report = classification_report(y_test, y_pred, output_dict=True)

    report_df = pd.DataFrame(report).transpose()

    report_path = os.path.join(MODEL_DIR, f"{name}_classification_report.csv")
    report_df.to_csv(report_path)

    # ================================
    # 📊 CONFUSION MATRIX (SAVE PNG)
    # ================================
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

    plt.title(f"Confusion Matrix - {name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    cm_path = os.path.join(MODEL_DIR, f"{name}_confusion_matrix.png")
    plt.savefig(cm_path)
    plt.close()

    

# ================================
# 🔥 FEATURE IMPORTANCE (TREE ONLY)
# ================================
    if hasattr(model, "feature_importances_"):
    
        importance = model.feature_importances_

        feature_names = preprocessor.get_feature_names_out()
    
        imp_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importance
        }).sort_values(by="importance", ascending=False)
    
        # Save CSV
        imp_df.to_csv(os.path.join(MODEL_DIR, f"{name}_feature_importance.csv"), index=False)
    
        # Plot
        plt.figure(figsize=(8,5))
        plt.barh(imp_df["feature"], imp_df["importance"])
        plt.title(f"Feature Importance - {name}")
        plt.gca().invert_yaxis()
    
        fi_path = os.path.join(MODEL_DIR, f"{name}_feature_importance.png")
        plt.savefig(fi_path)
        plt.close()
    print(f"\n{name}")
    print("Accuracy:", acc)
    print("ROC:", roc)
    print("CV:", cv)

    joblib.dump(model, os.path.join(MODEL_DIR, f"{name}.pkl"))

    results.append([name, acc, roc, cv])

# Save best model
best_model = max(results, key=lambda x: x[1])[0]
joblib.dump(joblib.load(os.path.join(MODEL_DIR, f"{best_model}.pkl")),
            os.path.join(MODEL_DIR, "best_model.pkl"))

joblib.dump(preprocessor, PREPROCESSOR_PATH)