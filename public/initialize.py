import streamlit as st


def setup(title: str):
    """设置全局样式、根据项目和环境获取全局数据."""
    st.set_page_config(
        page_title="ATool | 自动化测试小助手",
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.subheader(title)
    project = st.sidebar.selectbox("🚩 选择项目", ("AAA", "BBB", "CCC"), index=0)
    with st.sidebar:
        env = st.radio("🌦️ 执行环境", ("测试", "生产", "演示"))

    return project, env

