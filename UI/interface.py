# UI/interface.py
import sys
import os
import streamlit as st
<<<<<<< HEAD
import tempfile
import time
from pathlib import Path
=======
>>>>>>> 1f8a9ca78796d6addb3a8b807d3a6100e36ee739

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from LLM_feedback.got_feedback import get_feedback
<<<<<<< HEAD
from analysis.filler_counter import count_filler_words
from transcription.transcribe import transcribe_audio
from database.db_utils import save_transcript_and_feedback

# Set up Streamlit page config
st.set_page_config(
    page_title="🗣️ AI Public Speaking Coach",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
    }
    .feedback-box {
        background: #f8f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e3e6f0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎤 AI Public Speaking Coach</h1>
        <p>Get instant feedback on your presentations and improve your speaking skills</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("🎯 Analysis Options")
        analysis_type = st.selectbox(
            "Choose your input method:",
            ["📝 Text Input", "🎵 Audio Upload", "🎙️ Voice Recording"]
        )
        
        st.markdown("---")
        st.markdown("### 📊 Features")
        st.markdown("• **Speech Transcription**")
        st.markdown("• **Filler Word Detection**")
        st.markdown("• **AI-Powered Feedback**")
        st.markdown("• **Speaking Analytics**")
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.markdown("• Speak clearly and at a moderate pace")
        st.markdown("• Avoid excessive filler words")
        st.markdown("• Practice your delivery")
        st.markdown("• Review feedback regularly")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        if analysis_type == "📝 Text Input":
            st.subheader("📝 Enter Your Speech Text")
            
            # Example text
            with st.expander("📌 Example Input"):
                st.markdown("""
                *"Uh, I studied computer science and um, I worked on like a few AI projects, 
                you know, and so I think that um, the future of technology is really, 
                like, exciting and stuff."*
                """)
            
            # Text input
            transcript = st.text_area(
                "Your speech transcript:",
                height=200,
                placeholder="Paste your speech text here..."
            )
            
            if st.button("✨ Analyze Speech", use_container_width=True):
                if transcript.strip():
                    analyze_speech(transcript)
                else:
                    st.warning("⚠️ Please enter your transcript first.")

        elif analysis_type == "🎵 Audio Upload":
            st.subheader("🎵 Upload Audio File")
            
            uploaded_file = st.file_uploader(
                "Choose an audio file",
                type=['wav', 'mp3', 'm4a', 'flac'],
                help="Supported formats: WAV, MP3, M4A, FLAC"
            )
            
            if uploaded_file is not None:
                # Show file details
                file_details = {
                    "Filename": uploaded_file.name,
                    "File size": f"{uploaded_file.size / 1024:.2f} KB",
                    "File type": uploaded_file.type
                }
                st.json(file_details)
                
                if st.button("🎵 Transcribe & Analyze", use_container_width=True):
                    with st.spinner("Processing audio..."):
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_path = tmp_file.name
                        
                        try:
                            # Transcribe audio
                            transcript = transcribe_audio(tmp_path)
                            st.success("✅ Audio transcribed successfully!")
                            
                            # Analyze the transcript
                            analyze_speech(transcript)
                            
                        except Exception as e:
                            st.error(f"❌ Error processing audio: {str(e)}")
                        finally:
                            # Clean up temporary file
                            os.unlink(tmp_path)

        elif analysis_type == "🎙️ Voice Recording":
            st.subheader("🎙️ Record Your Speech")
            
            st.info("🎙️ Voice recording feature coming soon! For now, please use text input or audio upload.")
            
            # Placeholder for future voice recording implementation
            st.markdown("""
            **Future Features:**
            - Real-time voice recording
            - Live transcription
            - Instant feedback
            - Audio playback
            """)

    with col2:
        st.subheader("📊 Quick Stats")
        
        # Placeholder metrics (these would be populated with actual data)
        col2a, col2b = st.columns(2)
        
        with col2a:
            st.metric("Sessions", "0")
            st.metric("Avg. Score", "N/A")
        
        with col2b:
            st.metric("Filler Words", "0")
            st.metric("Words/Min", "N/A")

def analyze_speech(transcript):
    """Analyze speech and display results"""
    
    # Create progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Step 1: Analyze filler words
    status_text.text("Analyzing filler words...")
    progress_bar.progress(25)
    time.sleep(0.5)
    
    filler_count = count_filler_words(transcript)
    
    # Step 2: Get AI feedback
    status_text.text("Generating AI feedback...")
    progress_bar.progress(50)
    time.sleep(0.5)
    
    ai_feedback = get_feedback(transcript)
    
    # Step 3: Save to database
    status_text.text("Saving analysis...")
    progress_bar.progress(75)
    time.sleep(0.5)
    
    save_transcript_and_feedback(transcript, ai_feedback)
    
    # Step 4: Complete
    status_text.text("Analysis complete!")
    progress_bar.progress(100)
    time.sleep(0.5)
    
    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()
    
    # Display results
    st.success("✅ Analysis complete!")
    
    # Results in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📝 Transcript")
        st.markdown(f'<div class="feedback-box">{transcript}</div>', unsafe_allow_html=True)
        
        st.markdown("### 📊 Filler Word Analysis")
        filler_percentage = (filler_count / len(transcript.split())) * 100 if len(transcript.split()) > 0 else 0
        st.metric("Filler Words Found", filler_count)
        st.metric("Filler Word Percentage", f"{filler_percentage:.1f}%")
        
        if filler_count > 10:
            st.warning("⚠️ High number of filler words detected. Consider practicing to reduce them.")
        elif filler_count > 5:
            st.info("ℹ️ Moderate filler word usage. Room for improvement.")
        else:
            st.success("✅ Great job! Low filler word usage.")
    
    with col2:
        st.markdown("### 🧠 AI Feedback")
        st.markdown(f'<div class="feedback-box">{ai_feedback}</div>', unsafe_allow_html=True)
        
        # Word count and speaking time estimates
        word_count = len(transcript.split())
        estimated_time = word_count / 150  # Assuming 150 words per minute
        
        st.markdown("### 📈 Speaking Metrics")
        st.metric("Word Count", word_count)
        st.metric("Estimated Speaking Time", f"{estimated_time:.1f} minutes")
        
        # Suggestions based on analysis
        st.markdown("### 💡 Suggestions")
        suggestions = []
        if filler_count > 5:
            suggestions.append("Practice pausing instead of using filler words")
        if word_count < 50:
            suggestions.append("Consider adding more detail to your speech")
        if word_count > 500:
            suggestions.append("Your speech might be too long for the audience")
        
        for suggestion in suggestions:
            st.markdown(f"• {suggestion}")

if __name__ == "__main__":
    main()
=======


# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# ✅ Set up Streamlit page config
st.set_page_config(
    page_title="🗣️ AI Public Speaking Coach",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 AI Public Speaking Feedback")
st.subheader("Paste your transcript and get personalized feedback!")

# ✅ Example usage
with st.expander("📌 Example input"):
    st.markdown(
        """
        *Uh I studied computer science and um I 
        worked on like a few AI projects...*  
        Try copying your spoken response here to get AI-based coaching.
        """
    )

# ✅ Input box
transcript = st.text_area("📝 Your speech transcript:", height=200)

# ✅ Button and logic
if st.button("✨ Get Feedback"):
    if not transcript.strip():
        st.warning("⚠️ Please enter your transcript first.")
    else:
        with st.spinner("Analyzing your speech..."):
            feedback = get_feedback(transcript)
        st.success("✅ Feedback received!")
        st.markdown("### 🧠 AI Feedback:")
        st.write(feedback)
>>>>>>> 1f8a9ca78796d6addb3a8b807d3a6100e36ee739
