import json
from datetime import datetime

import streamlit as st
import pandas as pd

from data import examples
from public import initialize

project, env = initialize.setup(title="⛅ 报告汇总")


@st.cache_data
def read_examples_history():
    _history_data = json.load(open(examples.joinpath("history-trend.json"), "rb"))
    return pd.DataFrame(
        [list(data.get("data").values())[:-2] for data in _history_data],
        columns=[
            "failed",
            "broken",
            "skipped",
            "passed",
        ],
    )


history = read_examples_history()

latest = datetime.now()  # fake
st.markdown(f"最新执行日期: {latest.strftime('%Y-%m-%d %H:%M:%S')}")
col_date, *_ = st.columns(3)
d = col_date.date_input("选择报告日期", latest)
st.markdown(f"[在线报告](https://autotest-report.net/api/prod/standard/coor/{d.strftime('%Y%m%d%H%M%S')}/#)")

col1, col2, col3, *_ = st.columns(6)
col2.metric("通过率", "95%", "5%")
col1.metric("用例数", "500", "10")
col3.metric("失败率", "5%", "-5%")

col_area, col_results, *_ = st.columns(3)
col_area.area_chart(history, use_container_width=True)


@st.cache_data
def read_examples_behaviors():
    results = []
    _behaviors = json.load(open(examples.joinpath("behaviors.json"), "rb"))

    def read_behaviors(behaviors: dict):
        if isinstance(behaviors, dict):
            if children := behaviors.get("children"):
                read_behaviors(children)
            else:
                name = str(behaviors.get("name")).strip().replace("：", "#").replace(":", "#").replace("|", "#")
                try:
                    code, name, author = [case.strip() for case in name.split("#") if name.count("#") == 2]
                    if behaviors.get("status") == "failed":
                        results.append(
                            {
                                "编码": code,
                                "名称": name,
                                "状态": behaviors.get("status"),
                                "作者": author,
                            }
                        )
                except ValueError:
                    pass
        else:
            for behavior in behaviors:
                read_behaviors(behavior)
        return results

    return pd.DataFrame(read_behaviors(_behaviors))
