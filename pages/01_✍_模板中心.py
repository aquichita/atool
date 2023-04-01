import streamlit as st
import initialize
from utils import statics, case_template


initialize.setup()

templates = {
    "E2E": "E2ECaseTemplate.xlsx",
}
select_template, *_ = st.columns(6)
template = select_template.selectbox("🍪*用例模板*", ("E2E",), index=0)

with open(statics.joinpath(templates.get(template)), "rb") as file:
    st.download_button(
        label=f":arrow_down: {template} template",
        data=file,
        file_name=templates.get(template),
        mime="xlsx",
    )

col_file_uploader, *_ = st.columns(2)
uploaded_file = col_file_uploader.file_uploader(
    label=":green[Please upload case template.]",
    type="xlsx",
    accept_multiple_files=False,
)

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    content = case_template(file=file_bytes)
    st.success("Generate script success from case template!", icon="✅")
    st.code(body=content, language="python")
    st.balloons()
