from fastapi import FastAPI
from db import SessionLocal, init_db
from models import DailySales

app = FastAPI()
init_db()

@app.get("/daily-sales")
def get_daily_sales():
    db = SessionLocal()
    data = db.query(DailySales).all()
    db.close()

    return [
        {
            "date": row.date,
            "total_orders": row.total_orders,
            "total_revenue": row.total_revenue,
            "unique_customers": row.unique_customers
        }
        for row in data
    ]
