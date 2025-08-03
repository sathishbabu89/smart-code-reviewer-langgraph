# app.py

import streamlit as st
import zipfile
import tempfile
import os
from langgraph_review import run_code_review


st.set_page_config(page_title="Smart Code Review", layout="wide")
st.title("🧠 Smart Code Review App (Java)")

uploaded_file = st.file_uploader("Upload your zipped Java project", type=["zip"])

if uploaded_file:
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, "uploaded.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.read())
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        st.success("Project extracted. Running review agents...")

        # Run the LangGraph code review process
        with st.spinner("Analyzing your Java project..."):
            review_results = run_code_review(temp_dir)

        st.subheader("📋 Code Review Report")
        st.write(review_results)
