import streamlit as st

from database import (
    search_problems,
    get_topics,
    delete_problem
)

st.set_page_config(page_title="Browse Problems", page_icon="📚")

st.title("📚 Browse Problems")

search = st.text_input(
    "Search by title"
)

topics = ["All"] + get_topics()

selected_topic = st.selectbox(
    "Topic",
    topics
)

selected_difficulty = st.selectbox(
    "Difficulty",
    [
        "All",
        "Easy",
        "Medium",
        "Hard"
    ]
)

problems = search_problems(
    search_text=search,
    topic=selected_topic,
    difficulty=selected_difficulty
)

st.write(f"### {len(problems)} problem(s) found")

st.divider()

if len(problems) == 0:

    st.info("No problems found.")

else:

    for problem in problems:

        with st.container():

            c1, c2 = st.columns([5, 2])

            with c1:

                status = "✅" if problem["solved"] else "⬜"

                st.subheader(f"{status} {problem['title']}")

                st.write(
                    f"**Topic:** {problem['topic']}"
                )

                st.write(
                    f"**Difficulty:** {problem['difficulty']}"
                )

            with c2:

                solve_col, edit_col, delete_col = st.columns(3)

                with solve_col:

                    if st.button(
                        "Solve",
                        key=f"solve_{problem['id']}"
                    ):

                        st.session_state.problem_id = problem["id"]

                        st.switch_page(
                            "pages/Solve.py"
                        )

                with edit_col:

                    if st.button(
                        "Edit",
                        key=f"edit_{problem['id']}"
                    ):

                        st.session_state.problem_id = problem["id"]

                        st.switch_page(
                            "pages/Edit_Problem.py"
                        )

                with delete_col:

                    if st.button(
                        "Delete",
                        key=f"delete_{problem['id']}"
                    ):

                        delete_problem(problem["id"])

                        st.success("Problem deleted successfully!")

                        st.rerun()

            st.divider()
