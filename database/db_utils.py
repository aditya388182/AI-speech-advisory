<<<<<<< HEAD
# db_utils.py

from .db_setup import get_db_connection

def save_transcript_and_feedback(transcript: str, feedback: str, filler_count: int = 0):
    """Save transcript and feedback to SQLite database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO feedback (transcript, feedback, filler_count)
            VALUES (?, ?, ?)
        ''', (transcript, feedback, filler_count))
        
        conn.commit()
        conn.close()
        print("[INFO] Data saved to SQLite database.")
        
    except Exception as e:
        print(f"[ERROR] Failed to save to database: {e}")

def get_recent_feedback(limit: int = 10):
    """Get recent feedback entries from database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM feedback 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (limit,))
        
        results = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in results]
        
    except Exception as e:
        print(f"[ERROR] Failed to retrieve from database: {e}")
        return []
=======
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
>>>>>>> 1f8a9ca78796d6addb3a8b807d3a6100e36ee739
