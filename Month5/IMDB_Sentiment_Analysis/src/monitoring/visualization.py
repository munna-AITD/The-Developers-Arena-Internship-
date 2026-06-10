import os
import matplotlib.pyplot as plt


def plot_training_history(history):

    # Create directories if they don't exist
    os.makedirs("reports/figures", exist_ok=True)

    # Accuracy Plot
    plt.figure(figsize=(8, 5))

    plt.plot(history.history["accuracy"], label="Train Accuracy")
    plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Training vs Validation Accuracy")
    plt.legend()

    plt.savefig("reports/figures/accuracy_curve.png")

    plt.close()

    # Loss Plot
    plt.figure(figsize=(8, 5))

    plt.plot(history.history["loss"], label="Train Loss")
    plt.plot(history.history["val_loss"], label="Validation Loss")

    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training vs Validation Loss")
    plt.legend()

    plt.savefig("reports/figures/loss_curve.png")

    plt.close()