
import pandas as pd
from pathlib import Path

# Define the output directory
DATA_DIR = Path("data/raw")

# Create the directory if it doesn't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Financial report from System A
system_a = [
    {"transaction_id": "TXN001", "transaction_date": "2026-10-01", "customer_id": "C001", "amount": 1500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN002", "transaction_date": "2026-10-01", "customer_id": "C002", "amount": 2500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN003", "transaction_date": "2026-10-02", "customer_id": "C003", "amount": 3200.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN004", "transaction_date": "2026-10-02", "customer_id": "C004", "amount": 1800.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN005", "transaction_date": "2026-10-03", "customer_id": "C005", "amount": 4500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN006", "transaction_date": "2026-10-03", "customer_id": "C006", "amount": 2100.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN007", "transaction_date": "2026-10-04", "customer_id": "C007", "amount": 900.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN008", "transaction_date": "2026-10-04", "customer_id": "C008", "amount": 3700.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN009", "transaction_date": "2026-10-05", "customer_id": "C009", "amount": 1250.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN010", "transaction_date": "2026-10-05", "customer_id": "C010", "amount": 6000.00, "currency": "PHP", "status": "Completed"},
]

# Financial report from System B
system_b = [
    {"transaction_id": "TXN001", "transaction_date": "2026-10-01", "customer_id": "C001", "amount": 1500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN002", "transaction_date": "2026-10-01", "customer_id": "C002", "amount": 2500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN003", "transaction_date": "2026-10-02", "customer_id": "C003", "amount": 3500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN004", "transaction_date": "2026-10-03", "customer_id": "C004", "amount": 1800.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN005", "transaction_date": "2026-10-03", "customer_id": "C005", "amount": 4500.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN006", "transaction_date": "2026-10-03", "customer_id": "C006", "amount": 2100.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN008", "transaction_date": "2026-10-04", "customer_id": "C008", "amount": 3700.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN009", "transaction_date": "2026-10-05", "customer_id": "C009", "amount": 1250.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN010", "transaction_date": "2026-10-05", "customer_id": "C010", "amount": 6000.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN010", "transaction_date": "2026-10-05", "customer_id": "C010", "amount": 6000.00, "currency": "PHP", "status": "Completed"},
    {"transaction_id": "TXN011", "transaction_date": "2026-10-06", "customer_id": "C011", "amount": 2800.00, "currency": "PHP", "status": "Completed"},
]

# Convert the records into DataFrames
df_a = pd.DataFrame(system_a)
df_b = pd.DataFrame(system_b)

# Export the reports as CSV files
df_a.to_csv(DATA_DIR / "system_a.csv", index=False)
df_b.to_csv(DATA_DIR / "system_b.csv", index=False)

print("Sample financial reports generated successfully!")
print(f"System A records: {len(df_a)}")
print(f"System B records: {len(df_b)}")
