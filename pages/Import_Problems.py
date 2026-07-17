import streamlit as st
from database import add_problem

st.set_page_config(
    page_title="Import Problems",
    page_icon="📥"
)

st.title("📥 Import Problem Packs")

requests_problems = [
    {
        "title": "GET Request Basics",
        "topic": "Requests",
        "difficulty": "Easy",
        "description": """
Send a GET request to

https://jsonplaceholder.typicode.com/users

Print the JSON response.
""",
        "starter_code": """import requests

# Write your code here
""",
        "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.json())
""",
        "hint": "Use requests.get()."
    },

    {
        "title": "Response Status Code",
        "topic": "Requests",
        "difficulty": "Easy",
        "description": """
Print only the HTTP status code of a GET request.
""",
        "starter_code": """import requests
""",
        "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.status_code)
""",
        "hint": "Look at response.status_code."
    }
]
