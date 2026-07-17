import streamlit as st


def render():

    st.title("➕ Add Problem")

    title = st.text_input(
        "Title"
    )

    topic = st.text_input(
        "Topic"
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    description = st.text_area(
        "Description"
    )

    if st.button("Save Problem"):

        st.success(
            "Saving will be implemented in the next milestone."
        )
