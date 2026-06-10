from src.monitoring.metrics import load_metrics


def show_dashboard():

    metrics = load_metrics()

    print("\n===== MODEL DASHBOARD =====\n")

    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\n===========================\n")


if __name__ == "__main__":
    show_dashboard()