from openai import OpenAI
import os
from dotenv import load_dotenv
from transcription.transcribe import transcribe_audio
from analysis.filler_counter import count_filler_words

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_feedback(transcript):
    prompt = (
        "You are a public speaking coach. "
        "Give feedback on this response:\n\n"
        f"{transcript}"
    )

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content


transcript = transcribe_audio("recordings/user_audio.wav")

if transcript:
    print("\nTranscript:\n", transcript)
    feedback = count_filler_words(transcript)
    print("\nFiller Word Feedback:\n", feedback)
else:
    print("No transcript generated.")
