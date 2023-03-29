import streamlit as st
from curd import sample


st.set_page_config(
    page_title="ATool",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("📝脚本模板生成")

uploaded_file = st.file_uploader(
    label="上传用例附件",
    type="xlsx",
    accept_multiple_files=False,
)

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    st.code(body=sample.case_template(file=file_bytes), language="python")
