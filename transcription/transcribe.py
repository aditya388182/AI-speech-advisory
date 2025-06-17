import whisper
import os


def transcribe_audio(file_path="recordings/user_audio.wav", model_size="base"):
    if not os.path.exists(file_path):
        print(f"[INFO] Audio file '{file_path}' " "not found. Skipping transcription.")
        return ""

    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]


if __name__ == "__main__":
    transcript = transcribe_audio()
    print("\nTranscript:\n", transcript)
