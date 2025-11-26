import streamlit as st 
import pandas as pd
import requests

API = "http://localhost:8000"

st.title("orderlytics - daily sales")

if st.button("refresh data from API"):
    pass

try:
    r = requests.get(f"{API}/daily-sales").json()

    # FIX: pandas requires list of dicts
    if isinstance(r, dict):
        df = pd.DataFrame([r])
    else:
        df = pd.DataFrame(r)

    if not df.empty:
        st.dataframe(df)
        df["date"] = pd.to_datetime(df["date"])

        st.line_chart(df.set_index("date")[["total_revenue", "total_orders"]])
        st.bar_chart(df.set_index("date")["unique_customers"])
    else:
        st.info("no data yet - run ETL")

except Exception as e:
    st.error("API unreachable. start uvicorn api:app --reload")
    st.text(str(e))
