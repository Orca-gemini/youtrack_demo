#!/bin/bash
# Get the commit message
COMMIT_MESSAGE=$(git log -1 --pretty=%B)

# Run the Python script to create a YouTrack issue
python C:\Users\csyas\OneDrive\Documents\code\AutomateYoutrack\demoYoutrack.py "$COMMIT_MESSAGE"
