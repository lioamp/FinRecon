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

    # Convert transaction dates into datetime format
    report["transaction_date"] = pd.to_datetime(
        report["transaction_date"],
        errors="coerce"
    )

    # Convert transaction amounts into numeric values
    report["amount"] = pd.to_numeric(
        report["amount"],
        errors="coerce"
    )

    return report

def inspect_report(name: str, report: pd.DataFrame):

    duplicate_ids = report.loc[
        report["transaction_id"].duplicated(keep=False),
        "transaction_id"
    ].unique()

    print(f"\n{name} Inspection")
    print("-" * 35)

    print(f"Total records: {len(report)}")
    print(f"Missing values: {report.isna().sum().sum()}")
    print(f"Invalid dates: {report['transaction_date'].isna().sum()}")
    print(f"Invalid amounts: {report['amount'].isna().sum()}")
    print(f"Zero or negative amounts: {(report['amount'].notna() & (report['amount'] <= 0)).sum()}")

    print(f"Duplicate transaction IDs: {list(duplicate_ids)}")

def main():

    system_a = load_report("system_a.csv")
    system_b = load_report("system_b.csv")

    inspect_report("System A", system_a)
    inspect_report("System B", system_b)


if __name__ == "__main__":
    main()