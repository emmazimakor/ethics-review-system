import streamlit as st
from form_aggregator import aggregate_form_to_string
from risk_screening import pre_screen_risk
from rag.retriever import generate_report

st.title("Research Ethics Preliminary Review System")

with st.form("proposal_form"):
    question_1 = st.text_area("Research Aims and Objectives")
    question_2 = st.text_area("Participant Group and Recruitment")
    question_3 = st.text_area("Data Collection and Handling")
    submitted = st.form_submit_button("Submit for Preliminary Ethics Assessment")

if submitted:
    form_data = {
        "question_1": question_1,
        "question_2": question_2,
        "question_3": question_3
    }
    proposal_string = aggregate_form_to_string(form_data)
    risk_floor = pre_screen_risk(form_data)

    st.info(f"Pre-screening risk floor: {risk_floor}")

    with st.spinner("Generating assessment... this may take a minute"):
        report = generate_report(proposal_string, risk_floor)

    st.markdown(report)
