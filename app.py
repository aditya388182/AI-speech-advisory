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

    try:
        # Save the uploaded file
        audio_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(audio_path)

        # Transcribe audio
        transcript = transcribe_audio(audio_path)

        # Analyze filler words
        filler_analysis = count_filler_words(transcript)
        filler_count = sum(1 for word in transcript.lower().split() if word in ['um', 'uh', 'like', 'you', 'know', 'so', 'actually', 'basically', 'literally', 'well', 'okay', 'right'])

        # Get AI feedback
        ai_feedback = get_feedback(transcript)

        # Save to database
        save_transcript_and_feedback(transcript, ai_feedback, filler_count)

        # Clean up the uploaded file
        os.remove(audio_path)

        # Return JSON response
        return jsonify({
            "success": True,
            "transcript": transcript,
            "filler_analysis": filler_analysis,
            "ai_feedback": ai_feedback,
            "filler_count": filler_count
        })

    except Exception as e:
        # Clean up file if it exists
        if os.path.exists(audio_path):
            os.remove(audio_path)
        return jsonify({"error": f"Error processing audio: {str(e)}"}), 500


@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    """Analyze text input directly"""
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        transcript = data['text']
        
        # Analyze filler words
        filler_analysis = count_filler_words(transcript)
        filler_count = sum(1 for word in transcript.lower().split() if word in ['um', 'uh', 'like', 'you', 'know', 'so', 'actually', 'basically', 'literally', 'well', 'okay', 'right'])

        # Get AI feedback
        ai_feedback = get_feedback(transcript)

        # Save to database
        save_transcript_and_feedback(transcript, ai_feedback, filler_count)

        return jsonify({
            "success": True,
            "transcript": transcript,
            "filler_analysis": filler_analysis,
            "ai_feedback": ai_feedback,
            "filler_count": filler_count
        })

    except Exception as e:
        return jsonify({"error": f"Error analyzing text: {str(e)}"}), 500


@app.route("/health")
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "AI Speech Advisory is running"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
