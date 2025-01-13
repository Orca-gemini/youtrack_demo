import requests
import sys

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
        return response.json()["id"]  # Return issue ID for future updates
    elif response.status_code == 405:
        print("Method Not Allowed. Please check the endpoint and HTTP method.")
    else:
        print(f"Failed to create issue: {response.status_code}, {response.text}")
    return None

# def update_issue(issue_id, commit_message):
#     url = f"{INSTANCE_URL}/api/issues/{issue_id}/transitions"  # Correct endpoint for applying transitions
#     # Check if 'fix' is in the commit message to trigger an update
#     if 'fix' in commit_message.lower():
#         payload = {
#             "transition": {
#                 "name": "Fixed"  # YouTrack transition name (ensure it matches your setup)
#             }
#         }
#         response = requests.post(url, headers=headers, json=payload)
#         if response.status_code == 200:
#             print(f"Issue {issue_id} updated with 'fix' keyword.")
#         else:
#             print(f"Failed to update issue: {response.status_code}, {response.text}")
#     else:
#         print(f"No 'fix' keyword in commit message. No update triggered.")

def main():
    # Check if the commit message is passed as an argument
    if len(sys.argv) > 1:
        commit_message = sys.argv[1]
        # Check if the commit message contains 'create issue'
        if 'create issue' in commit_message.lower():
            print(f"Commit message contains 'create issue'. Proceeding to create an issue...")
            # Replace '0-0' with your project ID and create the issue
            issue_id = create_issue("0-0", "Test Issue Summary", "This is a test description.")
            if issue_id:
                update_issue(issue_id, commit_message)
        elif 'fix' in commit_message.lower():
            print(f"Commit message contains 'fix'. Updating the issue...")
            issue_id = "DEMO-26"  # Example issue ID (you can also extract this dynamically from the commit message)
            update_issue(issue_id, commit_message)
        else:
            print(f"Commit message does not contain 'create issue' or 'fix'. No action performed.")
    else:
        print("No commit message passed. Exiting.")

if __name__ == "__main__":
    main()
