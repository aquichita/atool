import streamlit as st
import streamlit.components.v1 as components
import tkinter

st.set_page_config(
    page_title="ATool",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

base = tkinter.Tk()
height = base.winfo_screenheight()
width = base.winfo_screenwidth()

# embed streamlit docs in a streamlit app
components.iframe(
    "https://autotest-report.going-link.net/api/test/standard/all-new/20230329085527/#",
    width=width*0.75,
    height=height*0.7,
    scrolling=False
)
