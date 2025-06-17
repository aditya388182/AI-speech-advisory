# analysis/analyze.py

def count_filler(transcript: str) -> str:
    """
    Count filler words in the transcript and give basic feedback.

    Args:
        transcript (str): The transcribed speech text.

    Returns:
        str: Summary of filler word usage.
    """
    if not transcript.strip():
        return "[INFO] Transcript is empty. Please try again with valid audio."

    # Common filler words to check for
    filler_words = [
        "um", "uh", "like", "you know", "so", "actually", "basically",
        "literally", "i mean", "well", "okay", "right"
    ]

    transcript_lower = transcript.lower()

    filler_counts = {}
    total_fillers = 0

    for word in filler_words:
        count = transcript_lower.count(word)
        if count > 0:
            filler_counts[word] = count
            total_fillers += count

    if total_fillers == 0:
        return "✅ Great job! No filler words detected."

    # Build the feedback summary
    summary_lines = [f"🗣️ Filler Words Detected: {total_fillers} total\n"]
    for word, count in filler_counts.items():
        summary_lines.append(f"- '{word}': {count} time(s)")

    return "\n".join(summary_lines)
