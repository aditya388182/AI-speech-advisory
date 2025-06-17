import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


def get_feedback(transcript):
    """Get AI feedback on speech transcript"""
    
    # If no API key is available, provide basic feedback
    if not TOGETHER_API_KEY:
        return get_basic_feedback(transcript)
    
    prompt = (
        "You are a public speaking coach. "
        "Give friendly, constructive feedback on the following response:\n\n"
        f"{transcript}"
    )

    try:
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
            },
            timeout=30  # Add timeout
        )

        # Debug: Print raw output if anything fails
        try:
            data = response.json()
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
            return get_basic_feedback(transcript)

        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]
        else:
            # Show helpful error message
            error_message = data.get("error", {}).get("message", "Unknown error")
            print(f"API Error: {error_message}")
            return get_basic_feedback(transcript)
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return get_basic_feedback(transcript)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return get_basic_feedback(transcript)


def get_basic_feedback(transcript):
    """Provide basic feedback when API is not available"""
    if not transcript or not transcript.strip():
        return "No transcript provided. Please try recording or uploading audio again."
    
    # Count words and provide basic feedback
    words = transcript.split()
    word_count = len(words)
    
    feedback = f"📝 Transcript Analysis:\n"
    feedback += f"• Word count: {word_count} words\n"
    
    if word_count < 10:
        feedback += "• Your speech is quite brief. Consider adding more detail to make your point clearer.\n"
    elif word_count < 50:
        feedback += "• Good length for a concise response. Make sure your main points are clear.\n"
    else:
        feedback += "• Good length! Your speech provides substantial content.\n"
    
    # Check for common speaking patterns
    transcript_lower = transcript.lower()
    
    if "um" in transcript_lower or "uh" in transcript_lower:
        feedback += "• Try to reduce filler words like 'um' and 'uh' for more confident delivery.\n"
    
    if transcript_lower.count(".") < 2:
        feedback += "• Consider breaking up long sentences for better clarity.\n"
    
    feedback += "\n💡 Tip: Practice speaking slowly and clearly. Take pauses between thoughts."
    
    return feedback
