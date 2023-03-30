import streamlit as st
from public import initialize
from utils import statics, case_template


initialize.setup(title="📝脚本模板生成")

with open(statics.joinpath("E2E测试用例模板.xlsx"), "rb") as file:
    st.download_button(
        label=":arrow_down: E2E用例模板",
        data=file,
        file_name="E2E测试用例模板.xlsx",
        mime="xlsx",
    )

col_file_uploader, *_ = st.columns(2)
uploaded_file = col_file_uploader.file_uploader(
    label="上传用例附件",
    type="xlsx",
    accept_multiple_files=False,
)

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    content = case_template(file=file_bytes)
    st.success("脚本模板生成成功.", icon="✅")
    st.code(body=content, language="python")
    st.balloons()
