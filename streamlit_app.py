import streamlit as st
import pandas as pd
import requests

API = "http://localhost:8000"

st.title("Orderlytics - Daily Sales Dashboard")

try:
    r = requests.get(f"{API}/daily-sales").json()
    df = pd.DataFrame(r)

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        st.dataframe(df)

        st.subheader("Revenue & Orders Over Time")
        st.line_chart(df.set_index("date")[["total_revenue", "total_orders"]])

        st.subheader("Unique Customers Over Time")
        st.bar_chart(df.set_index("date")[["unique_customers"]])

    else:
        st.info("No data available. Run ETL first.")

except Exception as e:
    st.error("API unreachable. Start FastAPI using: uvicorn api:app --reload")
    st.text(str(e))
