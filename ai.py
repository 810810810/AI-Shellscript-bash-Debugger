#!/usr/bin/env python3

import subprocess
import sys
from googleapiclient.discovery import build
import json

# Set up Google Custom Search API credentials
API_KEY = "YOUR_API_KEY"
CX = "YOUR_CX"

# Define a function to search the web and return the top result
def search(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CX).execute()
    items = res["items"]
    return items[0]["snippet"]

# Define a function to enter learning mode
def learning_mode():
    prompt = "Entering learning mode. Please enter a Bash script you're having trouble with: "
    script = input(prompt)
    result = subprocess.run(["shellcheck", "-f", "gcc", "-x", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        prompt = "Great news! Your script has no errors. Anything else I can help with?"
    else:
        prompt = f"Here's what I found: {result.stderr.decode()}. Would you like me to fix it?"
        response = input(prompt)
        if response.lower() in ["yes", "y"]:
            # Extract the error line and column numbers
            error = result.stderr.decode().split(":")[-2:]
            line = error[0]
            column = error[1]

            # Extract the error message and suggested fix
            error = error[0].split(":")[0]
            result = search(f"bash {error} error solution")
            fix = json.loads(result)["items"][0]["snippet"]

            # Ask the user to confirm the suggested fix
            prompt = f"I suggest the following fix for the error on line {line}, column {column}: {fix}. Would you like me to apply the fix?"
            response = input(prompt)
            if response.lower() in ["yes", "y"]:
                # Apply the fix using sed
                subprocess.run(["sed", "-i", f"{line}s/.*/{fix}/", script])
                prompt = "The fix has been applied. Anything else I can help with?"
            else:
                prompt = "Alright. Anything else I can help with?"
        else:
            prompt = "Alright. Anything else I can help with?"

    print(prompt)

# Define a function to start Bashdb debugger
def start_debugger():
    prompt = "Starting Bashdb debugger. Please enter the name of the script you want to debug: "
    script = input(prompt)
    subprocess.run(["bashdb", script])
    prompt = "Debugger session ended. Anything else I can help with?"
    print(prompt)

# Define a function to run the AI
def run():
    prompt = "Hello! How can I help you with your Bash script debugging?"
    print(prompt)
    while True:
        input_str = input()
        if "learning mode" in input_str:
            learning_mode()
        elif "start debugger" in input_str:
            start_debugger()
        else:
            print("I'm sorry, I didn't understand. Please try again.")

# If this script is being run as the main program, start the AI
if __name__ == "__main__":
    run()
