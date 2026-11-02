from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

REQUIRED_COLUMNS = [
    "transaction_id",
    "transaction_date",
    "customer_id",
    "amount",
    "currency",
    "status"
]


def load_report(file_name: str) -> pd.DataFrame:

    file_path = RAW_DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Report not found: {file_path}")

    report = pd.read_csv(file_path)

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in report.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return report


def main():

    system_a = load_report("system_a.csv")
    system_b = load_report("system_b.csv")

    print("System A loaded successfully!")
    print(f"Records: {len(system_a)}")
    print(system_a.head())

    print("\nSystem B loaded successfully!")
    print(f"Records: {len(system_b)}")
    print(system_b.head())


if __name__ == "__main__":
    main()