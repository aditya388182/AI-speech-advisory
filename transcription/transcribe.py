import whisper
import os

<<<<<<< HEAD
def transcribe_audio(file_path="recordings/user_audio.wav", model_size="base"):
    if not os.path.exists(file_path):
        print(f"[INFO] Audio file '{file_path}' not found. Skipping transcription.")
=======

def transcribe_audio(file_path="recordings/user_audio.wav", model_size="base"):
    if not os.path.exists(file_path):
        print(f"[INFO] Audio file '{file_path}' " "not found. Skipping transcription.")
>>>>>>> 1f8a9ca78796d6addb3a8b807d3a6100e36ee739
        return ""

    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]

<<<<<<< HEAD
=======

>>>>>>> 1f8a9ca78796d6addb3a8b807d3a6100e36ee739
if __name__ == "__main__":
    transcript = transcribe_audio()
    print("\nTranscript:\n", transcript)
