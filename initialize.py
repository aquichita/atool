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
