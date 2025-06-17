# 🗣️ AI Speech Advisory Tool

A lightweight AI-powered assistant that provides intelligent feedback on mock interview speech. This tool helps job seekers, students, and professionals improve their spoken communication by analyzing their voice, identifying filler words, and offering constructive feedback using large language models (LLMs).

---

## 🚀 Features

- 🎙️ Upload `.wav` or `.mp3` audio files
- 🧠 Transcribes speech using OpenAI Whisper
- 🔍 Detects filler words like "uh", "um", "like"
- 🤖 GPT-4 generates feedback on clarity, confidence, and structure
- 🔊 Optional voice-based feedback using TTS
- 🧾 Stores results in a local SQLite database

---

## 🧠 Tech Stack

| Category        | Tech Used                |
|----------------|--------------------------|
| Backend         | Python 3.x               |
| Transcription   | OpenAI Whisper           |
| NLP Evaluation  | OpenAI GPT-3.5 / GPT-4   |
| Speech Analysis | Filler word detection    |
| UI              | Streamlit / Flask (configurable) |
| Voice Output    | gTTS or pyttsx3 (optional) |
| Database        | SQLite (local storage)   |

---

## 🗂️ Folder Structure
