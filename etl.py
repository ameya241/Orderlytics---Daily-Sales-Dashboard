import pandas as pd
from db import SessionLocal, init_db
from models import OrderRaw, DailySales
from datetime import datetime

init_db()

def load_csv(filename):
    return pd.read_csv(filename)

def load_to_raw(df):
    db = SessionLocal()
    for _, row in df.iterrows():
        record = OrderRaw(
            date=row["date"],
            customer_id=int(row["customer_id"]),
            amount=float(row["amount"])
        )
        db.add(record)
    db.commit()
    db.close()

def transform_and_load_daily():
    db = SessionLocal()
    df = pd.read_sql("SELECT * FROM order_raw", db.bind)

    df["date"] = pd.to_datetime(df["date"])
    summary = df.groupby("date").agg(
        total_orders=("id", "count"),
        total_revenue=("amount", "sum"),
        unique_customers=("customer_id", "nunique")
    ).reset_index()

    db.query(DailySales).delete()

    for _, row in summary.iterrows():
        rec = DailySales(
            date=row["date"].date(),
            total_orders=int(row["total_orders"]),
            total_revenue=float(row["total_revenue"]),
            unique_customers=int(row["unique_customers"])
        )
        db.add(rec)

    db.commit()
    db.close()

if __name__ == "__main__":
    df1 = load_csv("orders_day1.csv")
    df2 = load_csv("orders_day2.csv")

    load_to_raw(df1)
    load_to_raw(df2)

    transform_and_load_daily()

    print("ETL Completed Successfully!")
