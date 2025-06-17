import pyttsx3


def speak(
        text: str,
        rate: int = 170,
        volume: float = 0.9,
        voice_index: int = 0
        ):
    """
    Converts text to speech using pyttsx3 (offline TTS engine).

    Args:
        text (str): The text to speak.
        rate (int): Speech rate (default 170).
        volume (float): Volume (0.0 to 1.0).
        voice_index (int): Index of the voice to use
        from the list of available voices.

    Returns:
        None
    """
    try:
        engine = pyttsx3.init()

        # Set rate
        engine.setProperty("rate", rate)

        # Set volume
        engine.setProperty("volume", volume)

        # Set voice
        voices = engine.getProperty("voices")
        if 0 <= voice_index < len(voices):
            engine.setProperty("voice", voices[voice_index].id)
        else:
            print(
                f"[WARN] Invalid voice index {voice_index}."
                "Using default voice.")

        # Speak the text
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"[ERROR] Failed to speak text: {e}")
  

if __name__ == "__main__":
    speak("Hello Aditya! Your TTS module is working perfectly.")
