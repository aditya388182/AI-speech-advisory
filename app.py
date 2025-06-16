from transcription.transcribe import transcribe_audio
from analysis.analyze import count_filler_words

transcript = transcribe_audio("recordings/user_audio.wav")

if transcript:
    print("\nTranscript:\n", transcript)
    feedback = count_filler_words(transcript)
    print("\nFiller Word Feedback:\n", feedback)
else:
    print("No transcript generated.")
