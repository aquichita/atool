import pandas as pd
import requests
import streamlit as st

import initialize

initialize.setup()


REPORT_BASE_URL = "https://allure-framework.github.io/allure-demo/5"
st.markdown(f"[![Report online.](https://img.shields.io/badge/report-allure-green)]({REPORT_BASE_URL})")


@st.cache_data
def read_history_form_allure():
    response = requests.get(f"{REPORT_BASE_URL}/widgets/history-trend.json")
    return {
        "history": response.json(),
    }


@st.cache_data
def read_suites_form_allure():
    response = requests.get(f"{REPORT_BASE_URL}/data/suites.json")
    return {
        "suites": response.json().get("children"),
    }


history = read_history_form_allure()

trend = [history.get("data") for history in history.get("history")]

metrics = trend[:2]
total1, total2 = totals = [history.get("total") for history in metrics]
rate1, rate2 = rates = [(history.get("passed") / history.get("total")) * 100 for history in metrics]

passed, failed, total, *_ = st.columns(6)
passed.metric("Passed", f"{rate1:.2f}%", f"{(rate1-rate2):.2f}%")
failed.metric("Failed", f"{(100-rate1):.2f}%", f"{(rate2-rate1):.2f}%")
total.metric("Total", f"{total1}", f"{total1-total2}")


table_history, table_failed = st.columns(2)
table_history.markdown("*执行汇总*")
table_history_data = pd.DataFrame(trend, columns=["passed", "failed", "broken", "skipped", "unknown", "total"])
table_history.write(table_history_data)

table_failed.markdown("*失败汇总*")
table_failed.write(table_history_data)
