from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OrderRaw(Base):
    __tablename__ = "order_raw"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    customer_id = Column(Integer)
    amount = Column(Float)

class DailySales(Base):
    __tablename__ = "daily_sales"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    total_orders = Column(Integer)
    total_revenue = Column(Float)
    unique_customers = Column(Integer)
