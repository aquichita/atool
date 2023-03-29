import numpy as np
import streamlit as st
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from public import config

config.style(title="⛅ 报告汇总")

JENKINS_JOB_URL = "http://localhost:7000/job"
basic = HTTPBasicAuth("admin", "75ea5044422d447f8ad625a0572847ec")


@st.cache_data
def from_jenkins_allure(project: str):
    url = f"{JENKINS_JOB_URL}/{project}/allure/widgets/history-trend.json"
    trend = requests.get(url, auth=basic).json()[:10]
    report_urls = [report.get("reportUrl") for report in trend]
    report_data = [report.get("data") for report in trend]
    passed = [report.get("passed") for report in report_data]
    total = [report.get("total") for report in report_data]

    rend = {
        "在线报告": report_urls,
        "用例总数": total,
        "执行成功": passed,
        "执行失败": [total - passed for passed, total in zip(passed, total)],
        "成功率": [f"{(passed / total) * 100:.2f}%" for passed, total in zip(passed, total)],
    }
    return {"history_trend": rend}


reports, trend, code = st.tabs(["报告汇总", "质量趋势", "代码规范"])

with reports:
    data = from_jenkins_allure(project="pytest-demo")
    history_trend = pd.DataFrame(
        data=data.get("history_trend"),
        index=None,
    )
    st.write(history_trend)

with trend:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

with code:
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)
