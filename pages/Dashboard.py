
import streamlit as st
from database import get_counts

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 Dashboard")

total, easy, medium, hard = get_counts()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Problems", total)
col2.metric("Easy", easy)
col3.metric("Medium", medium)
col4.metric("Hard", hard)

st.divider()

st.subheader("Welcome!")

st.write("""
This is your personal StrataScratch-like platform.

Use the sidebar to:

- 📚 Browse problems
- 💻 Solve problems
- ➕ Add new problems
""")

def update_problem(
    problem_id,
    title,
    topic,
    difficulty,
    description,
    starter_code,
    solution,
    hint
):
    conn = get_connection()

    conn.execute("""
        UPDATE problems
        SET
            title=?,
            topic=?,
            difficulty=?,
            description=?,
            starter_code=?,
            solution=?,
            hint=?
        WHERE id=?
    """, (
        title,
        topic,
        difficulty,
        description,
        starter_code,
        solution,
        hint,
        problem_id
    ))

    conn.commit()
    conn.close()
