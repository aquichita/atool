import pandas as pd
import streamlit as st
import initialize


initialize.setup()


@st.cache_resource
def read_script_urls_form_db(script: str):
    project = st.session_state.project
    return {}


template = {
    "接口名称": "工作台列表地址查询",
    "请求地址": "/app/example/workbench/list",
    "更新内容": "请求地址",
    "是否完成": False,
}

select_script, add_script, *_ = st.columns(8)
project_script = select_script.selectbox("🚀 选择迭代", ("SCRIPT-001",), index=0)
script = add_script.text_input(label="🚀 新增迭代")
script_urls = read_script_urls_form_db(project_script)

st.write("示例:")
st.write(template)

df = pd.DataFrame(
    data=[script_urls],
    columns=["接口名称", "请求地址", "更新内容", "是否完成"],
)
edited_df = st.experimental_data_editor(df, num_rows="dynamic")
name, url, content, finished = latest_row = edited_df.values[-1]
st.markdown(f"新增接口同步: {name}")
