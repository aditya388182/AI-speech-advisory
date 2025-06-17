# 🎤 AI Speech Advisory

Your personal AI-powered speaking coach that analyzes speech patterns, identifies filler words, and provides constructive feedback to improve your public speaking skills.

## ✨ Features

- **🎵 Audio Upload**: Support for WAV, MP3, M4A, and FLAC files
- **🎙️ Live Recording**: Record your speech directly in the browser
- **🤖 AI Analysis**: Advanced speech pattern recognition and feedback
- **📊 Filler Word Detection**: Identifies common filler words like "um", "uh", "like", etc.
- **💡 Smart Feedback**: Personalized suggestions to improve speaking skills
- **📱 Modern UI**: Beautiful, responsive interface
- **💾 Data Storage**: Save and review your speaking history

## 🚀 Quick Start

### Option 1: Flask Web App (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

# Open in browser: http://127.0.0.1:5001
```

### Option 2: Streamlit Dashboard
```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run UI/interface.py

# Open in browser: http://localhost:8501
```

### Option 3: Launcher Script
```bash
# Use the launcher to choose your interface
python run_app.py
```

## 🔧 Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Optional: Enhanced AI Feedback
For enhanced AI feedback, create a `.env` file:
```bash
# Copy the example file
cp env_example.txt .env

# Edit .env and add your Together AI API key
# Get a free API key at: https://together.ai/
TOGETHER_API_KEY=your_api_key_here
```

**Note**: The app works without an API key, but provides basic feedback instead of advanced AI analysis.

## 📁 Project Structure

```
AI-speech-advisory/
├── app.py                 # Main Flask application
├── run_app.py            # Launcher script
├── requirements.txt      # Python dependencies
├── analysis/            # Speech analysis modules
│   └── filler_counter.py
├── audio_upload/        # Audio processing
│   └── upload_audio.py
├── database/           # Database and templates
│   ├── db_setup.py
│   ├── db_utils.py
│   └── templates/
│       └── index.html
├── LLM_feedback/       # AI feedback generation
│   └── got_feedback.py
├── transcription/      # Audio transcription
│   └── transcribe.py
├── TTS/               # Text-to-speech (future)
│   └── speak.py
└── UI/                # Streamlit interface
    └── interface.py
```

## 🎯 How to Use

### Upload Audio File
1. Click "Choose File" or drag & drop an audio file
2. Supported formats: WAV, MP3, M4A, FLAC
3. Click "Analyze Speech"
4. View your results!

### Record Live
1. Click "Start Recording"
2. Speak clearly into your microphone
3. Click "Stop Recording" when done
4. View your analysis results

### Text Analysis
1. Type or paste your speech text
2. Click "Analyze Text"
3. Get instant feedback

## 🔍 Troubleshooting

### Analysis Not Working?
1. **Check Audio Quality**: Ensure your audio file contains clear speech
2. **File Format**: Use supported formats (WAV, MP3, M4A, FLAC)
3. **File Size**: Large files may take longer to process
4. **API Key**: For enhanced feedback, add your Together AI API key to `.env`

### Common Issues:
- **"Could not transcribe audio"**: Try a different audio file with clearer speech
- **"Analysis failed"**: Check your internet connection and try again
- **"Template not found"**: Ensure all files are in the correct directories

### Port Already in Use?
```bash
# Find process using port 5001
lsof -i :5001

# Kill the process
kill -9 <PID>

# Or use a different port
python app.py --port 5002
```

### Missing Dependencies?
```bash
# Reinstall requirements
pip install -r requirements.txt

# For PyAudio issues on macOS:
brew install portaudio
export LDFLAGS="-L/opt/homebrew/lib"
export CFLAGS="-I/opt/homebrew/include"
pip install pyaudio
```

## 🌐 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to platforms like:
- Render (recommended)
- Heroku
- Railway
- Vercel

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI Whisper for speech transcription
- Together AI for enhanced feedback
- Flask and Streamlit communities

---

**Ready to improve your speaking skills? Start analyzing your speech today!** 🎤✨