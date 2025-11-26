<h1>"Orderlytics---Daily-Sales-Dashboard"</h1> 
<h1>📌 Overview</h1>

Orderlytics is an end-to-end Data Engineering project designed to demonstrate real-world skills in:

🔹 ETL Pipelines
🔹 Data Modeling & SQL
🔹 FastAPI (Data Service Layer)
🔹 Streamlit Dashboard
🔹 Automation & Orchestration Ready
🔹 Clean, optimized & beginner-friendly code

This project simulates a real e-commerce order system with synthetic data → processes it → stores insights → exposes APIs → visualizes analytics.

      ┌──────────────┐
      │ generate_data │  🔹 creates synthetic orders (CSV)
      └───────┬──────┘
              │
              ▼
      ┌──────────────┐
      │     ETL.py    │  🔹 cleans → transforms → aggregates
      └───────┬──────┘
              │
              ▼
     ┌────────────────┐
     │   SQLite/DB    │  🔹 stores fact tables + metrics
     └───────┬────────┘
              │
              ▼
     ┌────────────────┐
     │   FastAPI API  │  🔹 exposes /daily-sales endpoint
     └───────┬────────┘
              │
              ▼
     ┌────────────────┐
     │ Streamlit UI   │  🔹 visual dashboard
     └────────────────┘

<h1>✨ Features</h1>
<h2>🔧 1. Synthetic Data Generation</h2>

Generates realistic order events

Random customers, prices, timestamps

Output: orders_day1.csv, orders_day2.csv

<h2>🧹 2. ETL Pipeline</h2>

Cleans CSV inputs

Handles missing values

Groups & aggregates daily KPIs

Writes output to database tables

<h2>🗄️ 3. SQL Database (SQLite)</h2>

Tables:

order_raw

daily_sales

Designed for analytics queries

<h2>⚡ 4. FastAPI Backend</h2>

API Endpoints:

Endpoint	Description
/daily-sales	Returns daily metrics (JSON)
/health	Health check
<h2>📊 5. Dashboard (Streamlit)</h2>

Interactive table
Line-charts: revenue / orders
Bar-charts: unique customers
API-connected

<h2>📦 Project Structure</h2>
project/
│── generate_data.py
│── etl.py
│── db.py
│── models.py
│── api.py
│── app.py     ← Streamlit dashboard
│── orders_day1.csv
│── orders_day2.csv
│── requirements.txt
│── README.md

<h2>🚀 How to Run</h2>
1️⃣ Install dependencies - 
pip install -r requirements.txt

2️⃣ Generate sample data - 
python generate_data.py

3️⃣ Run ETL - 
python etl.py

4️⃣ Start FastAPI - 
uvicorn api:app --reload --port 8000

5️⃣ Start Streamlit dashboard - 
streamlit run app.py

<h2>📈 Sample Dashboard Preview</h2>
<img width="1919" height="1079" alt="Screenshot 2025-11-26 135609" src="https://github.com/user-attachments/assets/62806089-609f-4bba-9136-80ae3bda9adf" />

<img width="1918" height="1079" alt="Screenshot 2025-11-26 135624" src="https://github.com/user-attachments/assets/03bdb476-7051-431e-afb5-be7b40de17e8" />




