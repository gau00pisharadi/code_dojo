import streamlit as st

from database import (
    get_problem,
    update_problem
)

st.set_page_config(
    page_title="Edit Problem",
    page_icon="✏",
    layout="wide"
)

st.title("✏ Edit Problem")

if "problem_id" not in st.session_state:
    st.error("No problem selected.")
    st.stop()

problem = get_problem(st.session_state.problem_id)

if problem is None:
    st.error("Problem not found.")
    st.stop()

with st.form("edit_problem_form"):

    title = st.text_input(
        "Title",
        value=problem["title"]
    )

    topic = st.text_input(
        "Topic",
        value=problem["topic"]
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"],
        index=["Easy", "Medium", "Hard"].index(problem["difficulty"])
    )

    description = st.text_area(
        "Description",
        value=problem["description"],
        height=250
    )

    starter_code = st.text_area(
        "Starter Code",
        value=problem["starter_code"],
        height=250
    )

    solution = st.text_area(
        "Official Solution",
        value=problem["solution"],
        height=250
    )

    hint = st.text_area(
        "Hint",
        value=problem["hint"],
        height=100
    )

    pack = st.text_input(
        "Problem Pack",
        value=problem["pack"] if problem["pack"] else ""
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

        update_problem(
            problem["id"],
            title,
            topic,
            difficulty,
            description,
            starter_code,
            solution,
            hint,
            pack
        )

        st.success("Problem updated successfully!")
        st.balloons()
