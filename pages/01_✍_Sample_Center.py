import streamlit as st
import initialize
from utils import statics, case_template


initialize.setup(title="📝Script sample from case template.")

with open(statics.joinpath("E2ECaseTemplate.xlsx"), "rb") as file:
    st.download_button(
        label=":arrow_down: E2ECaseTemplate.xlsx",
        data=file,
        file_name="E2ECaseTemplate.xlsx",
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
