import streamlit as st
from code_editor import code_editor

from database import (
    get_problem,
    normalize_code,
    update_problem_status,
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

problem = get_problem(st.session_state.problem_id)

if problem is None:
    st.error("Problem not found.")
    st.stop()

# -----------------------------
# Problem Header + Solved Checkbox
# -----------------------------

title_col, solved_col = st.columns([8, 2])

with title_col:
    st.header(problem["title"])

with solved_col:

    solved = st.checkbox(
        "Solved",
        value=bool(problem["solved"]) if "solved" in problem.keys() else False,
        key=f"solved_{problem['id']}"
    )

    current_status = bool(problem["solved"]) if "solved" in problem.keys() else False

    if solved != current_status:
        update_problem_status(problem["id"], solved)
        st.rerun()

# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Topic:** {problem['topic']}")

with col2:
    st.write(f"**Difficulty:** {problem['difficulty']}")

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

if not response:
    user_code = problem["starter_code"]
else:
    user_code = (
        response.get("text")
        or response.get("code")
        or problem["starter_code"]
    )

col1, col2, col3 = st.columns(3)

# -----------------------------

with col1:

    if st.button("✅ Submit"):

        user_ast = normalize_code(user_code)
        solution_ast = normalize_code(problem["solution"])

        if user_ast is None:
            st.error("Your code contains a syntax error.")
        elif solution_ast is None:
            st.error("Official solution contains invalid Python.")
        elif user_ast == solution_ast:
            st.success("Correct! 🎉")
        else:
            st.error("Incorrect ❌")
# -----------------------------

with col2:

    if st.button("💡 Hint"):

        if problem["hint"]:
            st.info(problem["hint"])
        else:
            st.warning("No hint available.")

# -----------------------------

with col3:

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
