import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


def get_feedback(transcript):
    prompt = (
        "You are a public speaking coach. "
        "Give friendly, constructive feedback on the following response:\n\n"
        f"{transcript}"
    )

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/Mistral-7B-Instruct-v0.2", 
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 500
        }
    )

    # Debug: Print raw output if anything fails
    try:
        data = response.json()
    except Exception as e:
        return f"❌ Error parsing JSON response: {e}"

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        # Show helpful error message
        error_message = data.get("error", {}).get("message", "Unknown error")
        return f"❌ API Error: {error_message}"
