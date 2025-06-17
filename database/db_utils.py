import firebase_admin
from firebase_admin import credentials, firestore
import datetime

cred = credentials.Certificate("firebase_key.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()


def save_transcript_and_feedback(transcript, feedback):
    data = {
        "transcript": transcript,
        "feedback": feedback,
        "timestamp": datetime.datetime.utcnow()
    }
    db.collection("speech_feedback").add(data)
