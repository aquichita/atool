import streamlit as st
from curd import sample
from public import initialize


initialize.setup(title="📝脚本模板生成")

with open(sample.statics.joinpath("E2E测试用例模板.xlsx"), "rb") as file:
    st.download_button(
        label=":arrow_down: E2E用例模板",
        data=file,
        file_name="E2E测试用例模板.xlsx",
        mime="xlsx",
    )

uploaded_file = st.file_uploader(
    label="上传用例附件",
    type="xlsx",
    accept_multiple_files=False,
)

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    content = sample.case_template(file=file_bytes)
    st.success("脚本模板生成成功.", icon="✅")
    st.code(body=content, language="python")
    st.balloons()
