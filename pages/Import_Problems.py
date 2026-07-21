
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

# Check folder exists
if not os.path.exists(PACKS_FOLDER):
    st.error("problem_packs folder not found.")
    st.stop()

# Find all CSV files
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

file_path = os.path.join(PACKS_FOLDER, selected_pack)

try:
    df = pd.read_csv(file_path)
    df = df.fillna("")
    st.write(df.columns.tolist())

    st.success(f"{len(df)} problems found.")

    st.dataframe(
        df[["title", "topic", "difficulty"]],
        use_container_width=True
    )

except Exception as e:
    st.error(f"Unable to read CSV.\n\n{e}")
    st.stop()

if st.button("📥 Import Selected Pack"):
    
    #clear_problems()

    imported = 0

    for _, row in df.iterrows():

        add_problem(
            row["title"],
            row["topic"],
            row["difficulty"],
            row["description"],
            row["starter_code"],
            row["solution"],
            row["hint"]
        )

        imported += 1

    st.success(f"Imported {imported} problems from {selected_pack}")
