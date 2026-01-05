import os
import sys
import requests
import json
import sys
sys.stdout.reconfigure(encoding="utf-8")

# Load env
env_path = os.path.join(os.path.dirname(__file__), "config.env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ[k] = v

API_KEY = os.getenv("OPENAI_API_KEY")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")

if not API_KEY:
    print("ERROR: OPENAI_API_KEY missing", file=sys.stderr)
    sys.exit(1)

user_text = sys.stdin.read()

# Convert escaped newlines to real newlines
user_text = user_text.replace("\\n", "\n").strip()

if not user_text:
    sys.exit(0)

url = "https://api.openai.com/v1/responses"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4.1-mini",
    "input": [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_text
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

data = response.json()

# Extract text safely
output_text = data["output"][0]["content"][0]["text"]

print(output_text)
