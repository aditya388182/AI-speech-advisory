import os
from flask import Flask, render_template, request
from transcription.transcribe import transcribe_audio
from analysis import filler_counter
from database.db_utils import save_transcript_and_feedback  # Uses Firebase

app = Flask(__name__)
UPLOAD_FOLDER = "recordings"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure recordings folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_audio():
    if "audio_file" not in request.files:
        return "No file uploaded", 400

    file = request.files["audio_file"]
    if file.filename == "":
        return "No selected file", 400

    # Save uploaded file
    audio_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(audio_path)

    # Transcribe
    transcript = transcribe_audio(audio_path)

    # Analyze filler words
    filler_count = filler_counter.count_filler(transcript)
    feedback = f"Filler word count: {filler_count}"

    # Save to Firebase
    save_transcript_and_feedback(transcript, feedback)

    # Return result
    return (
        f"<h3>Transcript:</h3><p>{transcript}</p>"
        f"<h3>Feedback:</h3><p>{feedback}</p>"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5002)
