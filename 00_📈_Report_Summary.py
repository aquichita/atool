import json
from datetime import datetime

import requests
import streamlit as st
import pandas as pd

import initialize

initialize.setup(title="⛅ Report Summary.")

REPORT_BASE_URL = "https://allure-framework.github.io/allure-demo/5"


@st.cache_data
def read_allure_report():
    history = requests.get(f"{REPORT_BASE_URL}/widgets/history-trend.json").json()
    return {
        "history": history,
    }


report = read_allure_report()
st.markdown(
    f"[![Report online.](https://img.shields.io/badge/report-allure-green)]({REPORT_BASE_URL})"
)

trend = [history.get("data") for history in report.get("history")]
trend2 = trend[:2]
totals = [history.get("total") for history in trend2]
rates = [(history.get("passed") / history.get("total")) * 100 for history in trend2]

passed, failed, total, *_ = st.columns(7)
passed.metric("Passed", f"{rates[0]:.2f}%", f"{(rates[0]-rates[1]):.2f}%")
failed.metric("Failed", f"{(100-rates[0]):.2f}%", f"{(rates[1]-rates[0]):.2f}%")
total.metric("Total", f"{totals[0]}", f"{totals[0]-totals[1]}")

st.markdown("*latest test history.*")
table, *_ = st.columns(2)
table.dataframe(trend)
