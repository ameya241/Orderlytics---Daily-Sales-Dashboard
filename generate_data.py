import csv
import random
from datetime import datetime, timedelta

def random_orders(start_date, days, n):
    rows = []
    for _ in range(n):
        ts = start_date + timedelta(seconds=random.randint(0, days * 86400))
        rows.append({
            "date": ts.strftime("%Y-%m-%d"),
            "customer_id": random.randint(1, 50),
            "amount": round(random.uniform(100, 5000), 2)
        })
    return rows

def write_csv(rows, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "customer_id", "amount"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    today = datetime.now()
    rows1 = random_orders(today - timedelta(days=2), days=1, n=1200)
    rows2 = random_orders(today - timedelta(days=1), days=1, n=900)

    write_csv(rows1, "orders_day1.csv")
    write_csv(rows2, "orders_day2.csv")
    print("CSV generated successfully!")
