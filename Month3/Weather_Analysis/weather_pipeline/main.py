from etl_pipeline import run_pipeline
from reporter import generate_report
from alerts import check_alerts

def main():
    run_pipeline()
    generate_report()
    check_alerts()

if __name__=="__main__":
    main()
