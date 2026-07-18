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

if "last_filters" not in st.session_state:
    st.session_state.last_filters = None

current_filters = (
    search,
    selected_topic,
    selected_difficulty
)

if current_filters != st.session_state.last_filters:
    st.session_state.page = 0
    st.session_state.last_filters = current_filters

# -----------------------------------

problems = search_problems(
    search_text=search,
    topic=selected_topic,
    difficulty=selected_difficulty
)

problems = search_problems(
    search_text=search,
    topic=selected_topic,
    difficulty=selected_difficulty
)

PAGE_SIZE = 20

if "page" not in st.session_state:
    st.session_state.page = 0

start = st.session_state.page * PAGE_SIZE
end = start + PAGE_SIZE

displayed_problems = problems[start:end]


st.write(f"### {len(problems)} problem(s) found")

st.divider()

if len(problems) == 0:

    st.info("No problems found.")

else:

    for problem in displayed_problems:

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

prev_col, page_col, next_col = st.columns([1, 2, 1])

with prev_col:
    if st.button("⬅ Previous") and st.session_state.page > 0:
        st.session_state.page -= 1
        st.rerun()

with page_col:
    total_pages = (len(problems) - 1) // PAGE_SIZE + 1
    st.markdown(
        f"<div style='text-align:center;'>Page {st.session_state.page + 1} of {total_pages}</div>",
        unsafe_allow_html=True,
    )

with next_col:
    if (
        st.button("Next ➡")
        and end < len(problems)
    ):
        st.session_state.page += 1
        st.rerun()
