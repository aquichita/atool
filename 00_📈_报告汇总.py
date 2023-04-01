import pandas as pd
import requests
import streamlit as st

import initialize

initialize.setup(title="⛅ 报告汇总")

select_project, select_env, _, passed, failed, total = st.columns(6)
project = select_project.selectbox("🚩项目", ("演示项目",), index=0)
env = select_env.selectbox("🌦️环境", ("测试", "生产", "演示"), index=0)

st.session_state.project = project
st.session_state.env = env

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

passed.metric("Passed", f"{rates[0]:.2f}%", f"{(rates[0]-rates[1]):.2f}%")
failed.metric("Failed", f"{(100-rates[0]):.2f}%", f"{(rates[1]-rates[0]):.2f}%")
total.metric("Total", f"{totals[0]}", f"{totals[0]-totals[1]}")


table_history, table_failed = st.columns(2)
table_history.markdown("*执行汇总*")
table_history.write(
    pd.DataFrame(
        trend,
        columns=["passed", "failed", "broken", "skipped", "unknown", "total"],
    )
)
table_failed.markdown("*失败汇总*")
table_failed.write(
    pd.DataFrame(
        trend,
        columns=["passed", "failed", "broken", "skipped", "unknown", "total"],
    )
)
