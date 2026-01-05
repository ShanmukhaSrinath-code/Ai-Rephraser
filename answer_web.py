import os
import sys
import requests

# Load env file
env_path = os.path.join(os.path.dirname(__file__), "config.env")
with open(env_path, "r") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            os.environ[key] = value

API_KEY = os.getenv("PERPLEXITY_API_KEY")

question = sys.stdin.read()

url = "https://api.perplexity.ai/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "sonar-pro",
    "messages": [
        {
            "role": "system",
            "content": "Answer using real-world sources. Provide a clear answer and list sources."
        },
        {
            "role": "user",
            "content": question
        }
    ],
    "temperature": 0.2
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

print(response.json()["choices"][0]["message"]["content"])
