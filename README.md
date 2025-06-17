<<<<<<< HEAD
# 🎤 AI Speech Advisory

Your Personal Speaking Coach - Get instant feedback on your presentations and improve your speaking skills with AI-powered analysis.

## ✨ Features

- **🎵 Audio Upload & Transcription** - Upload audio files (WAV, MP3, M4A, FLAC) for automatic transcription
- **📝 Text Input Analysis** - Directly paste your speech text for instant feedback
- **🧠 AI-Powered Feedback** - Get personalized suggestions to improve your speaking
- **📊 Filler Word Detection** - Identify and count filler words in your speech
- **📈 Speaking Analytics** - Track your speaking metrics and progress
- **💾 Database Storage** - Save your analysis history for tracking improvement
- **🎨 Modern UI** - Beautiful, responsive interface available in both web and dashboard formats

## 🚀 Quick Start

### Option 1: Easy Launcher (Recommended)
```bash
python run_app.py
```
This will give you a menu to choose between Flask web interface and Streamlit dashboard.

### Option 2: Manual Launch

#### Flask Web Interface
```bash
python app.py
```
Then open http://localhost:5000 in your browser.

#### Streamlit Dashboard
```bash
streamlit run UI/interface.py
```
Then open http://localhost:8501 in your browser.

## 📦 Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd AI-speech-advisory
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables** (optional)
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 🎯 How to Use

### 🌐 Flask Web Interface
1. **Upload Audio**: Drag and drop or click to upload an audio file
2. **Record Live**: Use the recording feature (coming soon)
3. **Get Analysis**: View transcript, filler word count, and AI feedback
4. **Track Progress**: All analyses are saved to the database

### 📊 Streamlit Dashboard
1. **Choose Input Method**: Select from text input, audio upload, or voice recording
2. **Enter Content**: Paste your speech text or upload an audio file
3. **View Results**: See comprehensive analysis with metrics and suggestions
4. **Monitor Stats**: Track your speaking performance over time

## 🏗️ Project Structure

```
AI-speech-advisory/
├── app.py                 # Main Flask application
├── run_app.py            # Application launcher
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── analysis/            # Speech analysis modules
│   └── filler_counter.py
├── audio_upload/        # Audio upload handling
│   └── upload_audio.py
├── database/           # Database and templates
│   ├── db_setup.py
│   ├── db_utils.py
│   └── templates/
│       └── index.html  # Flask frontend
├── LLM_feedback/       # AI feedback generation
│   └── got_feedback.py
├── recordings/         # Temporary audio storage
├── transcription/      # Speech-to-text conversion
│   └── transcribe.py
├── TTS/               # Text-to-speech (future)
│   └── speak.py
└── UI/                # User interface modules
    └── interface.py   # Streamlit dashboard
```

## 🎨 Frontend Features

### Modern Web Interface (Flask)
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Drag & Drop**: Easy file upload with visual feedback
- **Real-time Processing**: Live progress indicators
- **Beautiful UI**: Modern gradient design with animations
- **Interactive Elements**: Hover effects and smooth transitions

### Interactive Dashboard (Streamlit)
- **Multiple Input Methods**: Text, audio upload, voice recording
- **Progress Tracking**: Visual progress bars and status updates
- **Comprehensive Metrics**: Detailed speaking analytics
- **Smart Suggestions**: AI-powered improvement tips
- **Sidebar Navigation**: Easy access to features and tips

## 🔧 Configuration

### Supported Audio Formats
- WAV (.wav)
- MP3 (.mp3)
- M4A (.m4a)
- FLAC (.flac)

### Database
The application uses SQLite for data storage. The database file (`feedback.db`) is automatically created when you first run the application.

### API Keys
For AI feedback functionality, you'll need an OpenAI API key. Set it in your environment variables or `.env` file.

## 🛠️ Development

### Running in Development Mode
```bash
# Flask with debug mode
export FLASK_ENV=development
python app.py

# Streamlit with debug
streamlit run UI/interface.py --logger.level debug
```

### Adding New Features
1. **Frontend**: Modify `database/templates/index.html` for Flask or `UI/interface.py` for Streamlit
2. **Backend**: Add new routes in `app.py` or functions in the respective modules
3. **Database**: Update `database/db_utils.py` for new data models

## 📊 Analysis Features

### Filler Word Detection
- Identifies common filler words: "um", "uh", "like", "you know", etc.
- Calculates filler word percentage
- Provides suggestions for improvement

### AI Feedback
- Content analysis and suggestions
- Speaking style recommendations
- Structure and flow improvements
- Confidence-building tips

### Speaking Metrics
- Word count and speaking time estimates
- Filler word frequency
- Speaking pace analysis
- Progress tracking over time

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check the console output for error messages
2. Ensure all dependencies are installed
3. Verify your API keys are set correctly
4. Check that audio files are in supported formats

## 🎯 Roadmap

- [ ] Real-time voice recording
- [ ] Advanced speech analytics
- [ ] Multi-language support
- [ ] Export reports
- [ ] Mobile app
- [ ] Integration with presentation software

---

**Made with ❤️ for better public speaking**
=======
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
>>>>>>> 1f8a9ca78796d6addb3a8b807d3a6100e36ee739

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
