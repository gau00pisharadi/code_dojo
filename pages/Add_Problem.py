from database import create_tables

create_tables()
import streamlit as st

from database import add_problem

st.set_page_config(
    page_title="Add Problem",
    page_icon="➕",
    layout="wide"
)

st.title("➕ Add Problem")

with st.form("add_problem_form"):

    title = st.text_input("Title")

    topic = st.text_input("Topic")

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    description = st.text_area(
        "Description",
        height=250
    )

    starter_code = st.text_area(
        "Starter Code",
        height=250
    )

    solution = st.text_area(
        "Official Solution",
        height=250
    )

    hint = st.text_area(
        "Hint",
        height=100
    )

    submitted = st.form_submit_button("💾 Save Problem")

if submitted:

    if (
        title.strip() == ""
        or topic.strip() == ""
        or description.strip() == ""
        or solution.strip() == ""
    ):

        st.error("Please fill all required fields.")

    else:

        add_problem(
            title,
            topic,
            difficulty,
            description,
            starter_code,
            solution,
            hint
        )

        st.success("Problem added successfully!")

        st.balloons()
