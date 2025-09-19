# src/transcription.py
import whisper

def load_model(model_size="base"):
    """Load a Whisper model."""
    return whisper.load_model(model_size)

def transcribe_audio(model, filepath, language="it"):
    """Transcribe audio with Whisper."""
    result = model.transcribe(filepath, language=language)
    return result["text"]   # <-- return only the text
    # return result["text"], result["segments"]  # <-- return text and segments if needed