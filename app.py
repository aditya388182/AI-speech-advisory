import os
import json
from flask import Flask, render_template, request, redirect, jsonify
from transcription.transcribe import transcribe_audio
from analysis.filler_counter import count_filler_words
from database.db_utils import save_transcript_and_feedback
from LLM_feedback.got_feedback import get_feedback

app = Flask(__name__, template_folder='database/templates')
UPLOAD_FOLDER = "recordings"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_audio():
    if "audio_file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["audio_file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Check file extension
    allowed_extensions = {'.wav', '.mp3', '.m4a', '.flac'}
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in allowed_extensions:
        return jsonify({"error": "Invalid file type. Please upload WAV, MP3, M4A, or FLAC files."}), 400

    audio_path = None
    try:
        # Save the uploaded file
        audio_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(audio_path)

        # Transcribe audio
        print(f"[INFO] Transcribing audio file: {audio_path}")
        transcript = transcribe_audio(audio_path)
        
        if not transcript or not transcript.strip():
            return jsonify({
                "success": False,
                "error": "Could not transcribe audio. Please ensure the audio file contains clear speech and try again."
            }), 400

        # Analyze filler words
        print(f"[INFO] Analyzing filler words in transcript")
        filler_analysis = count_filler_words(transcript)
        filler_count = sum(1 for word in transcript.lower().split() if word in ['um', 'uh', 'like', 'you', 'know', 'so', 'actually', 'basically', 'literally', 'well', 'okay', 'right'])

        # Get AI feedback
        print(f"[INFO] Generating AI feedback")
        ai_feedback = get_feedback(transcript)

        # Save to database
        print(f"[INFO] Saving to database")
        save_transcript_and_feedback(transcript, ai_feedback, filler_count)

        # Return JSON response
        return jsonify({
            "success": True,
            "transcript": transcript,
            "filler_analysis": filler_analysis,
            "ai_feedback": ai_feedback,
            "filler_count": filler_count
        })

    except Exception as e:
        print(f"[ERROR] Error processing audio: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"Error processing audio: {str(e)}. Please try again with a different audio file."
        }), 500
    finally:
        # Clean up the uploaded file
        if audio_path and os.path.exists(audio_path):
            try:
                os.remove(audio_path)
                print(f"[INFO] Cleaned up temporary file: {audio_path}")
            except Exception as e:
                print(f"[WARNING] Could not remove temporary file {audio_path}: {e}")


@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    """Analyze text input directly"""
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        transcript = data['text']
        
        if not transcript or not transcript.strip():
            return jsonify({
                "success": False,
                "error": "Please provide some text to analyze."
            }), 400
        
        # Analyze filler words
        print(f"[INFO] Analyzing filler words in text input")
        filler_analysis = count_filler_words(transcript)
        filler_count = sum(1 for word in transcript.lower().split() if word in ['um', 'uh', 'like', 'you', 'know', 'so', 'actually', 'basically', 'literally', 'well', 'okay', 'right'])

        # Get AI feedback
        print(f"[INFO] Generating AI feedback for text input")
        ai_feedback = get_feedback(transcript)

        # Save to database
        print(f"[INFO] Saving text analysis to database")
        save_transcript_and_feedback(transcript, ai_feedback, filler_count)

        return jsonify({
            "success": True,
            "transcript": transcript,
            "filler_analysis": filler_analysis,
            "ai_feedback": ai_feedback,
            "filler_count": filler_count
        })

    except Exception as e:
        print(f"[ERROR] Error analyzing text: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"Error analyzing text: {str(e)}"
        }), 500


@app.route("/health")
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "AI Speech Advisory is running"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
