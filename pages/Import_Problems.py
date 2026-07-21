import os

import pandas as pd
import streamlit as st

from database import add_problem, clear_problems

st.set_page_config(
    page_title="Import Problems",
    page_icon="📥"
)

st.title("📥 Import Problem Packs")

PACKS_FOLDER = "problem_packs"

if not os.path.exists(PACKS_FOLDER):
    st.error("problem_packs folder not found.")
    st.stop()

csv_files = sorted(
    [f for f in os.listdir(PACKS_FOLDER) if f.endswith(".csv")]
)

if not csv_files:
    st.warning("No CSV files found inside problem_packs.")
    st.stop()

selected_pack = st.selectbox(
    "Choose a problem pack",
    csv_files
)

pack = os.path.splitext(selected_pack)[0]

file_path = os.path.join(PACKS_FOLDER, selected_pack)

try:
    df = pd.read_csv(file_path)
    df = df.fillna("")

    st.success(f"{len(df)} problems found.")

    with st.expander("Preview"):
        st.write(df.columns.tolist())
        st.dataframe(
            df,
            use_container_width=True
        )

except Exception as e:
    st.error(f"Unable to read CSV.\n\n{e}")
    st.stop()

if st.button("📥 Import Selected Pack"):

    # Uncomment to wipe the database before importing
    # clear_problems()

    imported = 0

    for _, row in df.iterrows():

        add_problem(
            row["title"],
            row["topic"],
            row["difficulty"],
            row["description"],
            row["starter_code"],
            row["solution"],
            row["hint"],
            pack,
        )

        imported += 1

    st.success(
        f"Imported {imported} problems from '{pack}'."
    )
