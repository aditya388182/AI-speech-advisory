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