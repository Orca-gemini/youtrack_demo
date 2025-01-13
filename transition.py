import requests

# Replace with your actual API token
YOUR_API_TOKEN = "perm:YWRtaW4=.NDUtMQ==.S5cuv9wzu2MShgYAy5B2kBKqGbWgrG"

# Function to get available transitions
def get_available_transitions(issue_id):
    url = f"https://gemini3.myjetbrains.com/youtrack/api/issues/{issue_id}/transitions"
    headers = {"Authorization": f"Bearer {YOUR_API_TOKEN}", "Content-Type": "application/json"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        transitions = response.json()
        print(f"Available transitions for issue {issue_id}: {transitions}")
        return transitions
    else:
        print(f"Failed to get transitions: {response.status_code}, {response.text}")
        return []

# Function to transition the issue based on commit message
def transition_issue(issue_id, commit_message):
    transitions = get_available_transitions(issue_id)
    
    # Check if 'fix' or 'resolved' is in the commit message to trigger the transition
    if 'fix' in commit_message.lower():
        state = "In Progress"  # Replace with correct state from available transitions
    elif 'resolved' in commit_message.lower():
        state = "Resolved"  # Replace with correct state from available transitions
    else:
        print(f"No transition for commit message: {commit_message}")
        return
    
    # Find the corresponding transition ID for the state
    for transition in transitions:
        if state in transition['name']:  # Match the state name
            transition_id = transition['id']
            break
    else:
        print(f"No matching transition found for state: {state}")
        return
    
    # Payload with the transition ID
    payload = {
        "transition": {"id": transition_id}
    }
    
    url = f"https://gemini3.myjetbrains.com/youtrack/api/issues/{issue_id}/transitions"
    response = requests.post(url, headers={"Authorization": f"Bearer {YOUR_API_TOKEN}", "Content-Type": "application/json"}, json=payload)
    
    if response.status_code == 200:
        print(f"Issue {issue_id} transitioned to {state}.")
    else:
        print(f"Failed to transition issue: {response.status_code}, {response.text}")

# Example usage
commit_message = "Fixed bug with login form #DEMO-04"  # Example commit message with issue ID
issue_id = "DEMO-04"  # The ID of the issue you're working with

transition_issue(issue_id, commit_message)
