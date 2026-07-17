import streamlit as st

from src.database.init_db import init_database
from src.ui.sidebar import render_sidebar

from src.ui.pages import dashboard
from src.ui.pages import browse
from src.ui.pages import add_problem


st.set_page_config(
    page_title="CodeDojo",
    page_icon="🥋",
    layout="wide"
)


init_database()


page = render_sidebar()


if page == "Dashboard":
    dashboard.render()

elif page == "Browse Problems":
    browse.render()

elif page == "Add Problem":
    add_problem.render()
