import requests

# Configuration
INSTANCE_URL = "https://gemini3.myjetbrains.com/youtrack"  # Correct base URL
API_TOKEN = "perm:YWRtaW4=.NDUtMQ==.S5cuv9wzu2MShgYAy5B2kBKqGbWgrG"
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_issue(project_id, summary, description):
    url = f"{INSTANCE_URL}/api/issues"  # Correct endpoint to create an issue
    payload = {
        "project": {"id": project_id},
        "summary": summary,
        "description": description
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code in [200, 201]:
        print("Issue created successfully!")
        print("Issue ID:", response.json()["id"])  # Show the created issue's ID
    elif response.status_code == 405:
        print("Method Not Allowed. Please check the endpoint and HTTP method.")
    else:
        print(f"Failed to create issue: {response.status_code}, {response.text}")

# Replace '0-0' with your project ID
create_issue("0-0", "Test Issue Summary", "This is a test description.")

