# db_utils.py

from db_setup import db

def save_transcript_and_feedback(transcript: str, feedback: str):
    doc_ref = db.collection("voice_feedback").document()
    doc_ref.set({
        "transcript": transcript,
        "feedback": feedback
    })
    print("[INFO] Data saved to Firestore.")