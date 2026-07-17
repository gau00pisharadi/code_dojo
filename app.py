import streamlit as st

from database import create_tables

st.set_page_config(
    page_title="CodeDojo",
    page_icon="🥋",
    layout="wide",
)

create_tables()

st.title("🥋 CodeDojo")

st.markdown(
    """
Welcome to **CodeDojo**.

Use the sidebar to:

- 📊 Dashboard
- 📚 Browse Problems
- 💻 Solve Problems
- ➕ Add Problem
"""
)

st.success("Database initialized successfully.")
