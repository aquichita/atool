from typing import Literal

import streamlit as st


def setup(layout: Literal["centered", "wide"] = "wide"):
    """global setup. include icon,title,width,project,env."""
    st.set_page_config(
        page_title="ATool | 自动化测试小助手",
        page_icon="🏆",
        layout=layout,
        initial_sidebar_state="auto",
    )
    with st.sidebar:
        project = st.selectbox("🚩 选择项目", ("演示项目",), index=0)
        env = st.selectbox("🌦️ 选择环境", ("测试", "生产", "演示"), index=0)

        st.session_state.project = project
        st.session_state.env = env

