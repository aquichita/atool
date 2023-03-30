import streamlit as st


def setup(title: str):
    """global setup. include icon,title,width,project,env."""
    st.set_page_config(
        page_title="ATool | automation handler",
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.subheader(title)
    project = st.sidebar.selectbox("🚩 Select Project.", ("allure-demo",), index=0)
    with st.sidebar:
        env = st.radio("🌦️ Env", ("test", "prod", "demo"))

    st.session_state.project = project
    st.session_state.env = env

