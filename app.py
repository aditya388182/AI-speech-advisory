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
from flask import Flask, render_template, request, redirect
import os
from transcription.transcribe import transcribe_audio
from analysis.analyze import count_fillers
from database.db_utils import save_transcript_and_feedback

app = Flask(__name__)
UPLOAD_FOLDER = "recordings"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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

    audio_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(audio_path)

    # Transcribe
    transcript = transcribe_audio(audio_path)

    # Analyze (filler words)
    filler_count = count_fillers(transcript)
    feedback = f"Filler word count: {filler_count}"

    # Save to DB
    save_transcript_and_feedback(transcript, feedback)

    return f"<h3>Transcript:</h3><p>{transcript}</p><h3>Feedback:</h3><p>{feedback}</p>"

if __name__ == "__main__":
    app.run(debug=True)