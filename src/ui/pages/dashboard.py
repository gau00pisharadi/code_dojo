import streamlit as st


def render():

    st.title("🏠 Dashboard")

    st.info("Welcome to CodeDojo!")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Problems",
        0
    )

    c2.metric(
        "Solved",
        0
    )

    c3.metric(
        "Streak",
        0
    )
