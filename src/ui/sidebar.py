import streamlit as st


def render_sidebar():

    st.sidebar.title("CodeDojo")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Browse Problems",
            "Add Problem"
        ]
    )

    return page
