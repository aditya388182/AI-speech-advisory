# UI/interface.py
import sys
import os
import streamlit as st

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from LLM_feedback.got_feedback import get_feedback


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
