import streamlit as st
from code_editor import code_editor

from database import (
    get_problem,
    normalize_code,
)

st.set_page_config(
    page_title="Solve Problem",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Solve Problem")

# -----------------------------

if "problem_id" not in st.session_state:

    st.warning("Please select a problem from Browse Problems.")

    st.stop()

# -----------------------------

problem = get_problem(
    st.session_state.problem_id
)

if problem is None:

    st.error("Problem not found.")

    st.stop()

# -----------------------------

st.header(problem["title"])

c1, c2 = st.columns(2)

c1.write(f"**Topic:** {problem['topic']}")
c2.write(f"**Difficulty:** {problem['difficulty']}")

st.divider()

st.subheader("Description")

st.markdown(problem["description"])

st.divider()

st.subheader("Your Solution")

response = code_editor(
    problem["starter_code"],
    lang="python",
    theme="default",
    height=[20, 350],
)

user_code = response.get("text", ""))

c1, c2, c3 = st.columns(3)

# -----------------------------

with c1:

    if st.button("✅ Submit"):

        if normalize_code(user_code) == normalize_code(problem["solution"]):

            st.success("Correct! 🎉")

        else:

            st.error("Incorrect ❌")

# -----------------------------

with c2:

    if st.button("💡 Hint"):

        if problem["hint"]:

            st.info(problem["hint"])

        else:

            st.warning("No hint available.")

# -----------------------------

with c3:

    if st.button("👀 Reveal Solution"):

        st.code(
            problem["solution"],
            language="python"
        )

st.divider()

with st.expander("Starter Code"):

    st.code(
        problem["starter_code"],
        language="python"
    )
