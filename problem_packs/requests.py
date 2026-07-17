requests_problems = [

{
    "title": "GET Request Basics",
    "topic": "Requests",
    "difficulty": "Easy",
    "description": """Send a GET request to:

https://jsonplaceholder.typicode.com/posts

Print the JSON response.
""",
    "starter_code": """import requests

# Write your code here
""",
    "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.json())
""",
    "hint": "Use requests.get() followed by response.json()."
},

{
    "title": "Response Status Code",
    "topic": "Requests",
    "difficulty": "Easy",
    "description": """Send a GET request to:

https://jsonplaceholder.typicode.com/posts

Print only the HTTP status code.
""",
    "starter_code": """import requests

# Write your code here
""",
    "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.status_code)
""",
    "hint": "Look at the response.status_code attribute."
},

{
    "title": "Print Response Text",
    "topic": "Requests",
    "difficulty": "Easy",
    "description": """Send a GET request and print the raw response body instead of converting it to JSON.
""",
    "starter_code": """import requests

# Write your code here
""",
    "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.text)
""",
    "hint": "Use response.text."
},

{
    "title": "Print Response Headers",
    "topic": "Requests",
    "difficulty": "Easy",
    "description": """Send a GET request and print all response headers.
""",
    "starter_code": """import requests

# Write your code here
""",
    "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.headers)
""",
    "hint": "Headers behave like a dictionary."
},

{
    "title": "Content-Type Header",
    "topic": "Requests",
    "difficulty": "Easy",
    "description": """Send a GET request and print only the Content-Type header returned by the server.
""",
    "starter_code": """import requests

# Write your code here
""",
    "solution": """import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.headers["Content-Type"])
""",
    "hint": "Access the required header using response.headers."
},

]
