import streamlit as st
import requests
import time

st.set_page_config(page_title="Autonomous Data Analyst")

st.title("AUTONOMOUS DATA ANALYST")
st.write("Get it analyzed for you")

# 🔥 Session state
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = None


file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx", "xls"])

if file:
    st.session_state.file_uploaded = file
    st.write(f"> File selected: {file.name}")

    proceed = st.radio("Proceed?", ["Yes", "No"])

    if proceed == "Yes":
        if st.button("Start Analysis"):
            terminal = st.empty()
            logs = []

            def add_log(text):
                logs.append(text)
                terminal.code("\n".join(logs))

            add_log("> Initializing system...")

            files = {"file": file}

            response = requests.post("http://127.0.0.1:8000/analyze-file", files=files)

            data = response.json()

            for step in data["steps"]:
                time.sleep(1)
                add_log(f"> Running {step['step']}...")
                time.sleep(0.5)
                add_log("✔ Completed")
                add_log(step["output"])

            add_log("> Analysis complete ✅")

            report_id = data["report_id"]
            st.session_state.report_id = report_id

            # ✅ Enable download after analysis
            st.session_state.analysis_done = True

            if st.session_state.analysis_done:
                url = f"http://127.0.0.1:8000/download-report/{st.session_state.report_id}"

                response = requests.get(url)

                st.download_button(
                    label="Download Report",
                    data=response.content,
                    file_name="analysis_report.pdf",
                    mime="application/pdf",
                )
