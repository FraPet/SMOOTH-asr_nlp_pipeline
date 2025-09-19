# main.py
import os
from src import transcription, postprocessing, formatter, utils
from src.config import LANGUAGE

# main.py
import os
from src import transcription, postprocessing, formatter, utils
from src.config import LANGUAGE

def main():
    # Input audio depending on LANGUAGE
    if LANGUAGE == "it":
        audio_path = os.path.join("data", "example_audio", "demo-it_16k-mono.wav")
        output_path = os.path.join("data", "outputs", "demo-it_output.txt")
    else:
        audio_path = os.path.join("data", "example_audio", "demo-en_16k-mono.wav")
        output_path = os.path.join("data", "outputs", "demo-en_output.txt")

    # Load Whisper model
    model = transcription.load_model("tiny")

    # Transcribe
    text = transcription.transcribe_audio(model, audio_path, language=LANGUAGE)

    # Tokenize + POS tagging
    tokens = postprocessing.process_text(text, language=LANGUAGE)

    # Format as *PAR: lines
    formatted = formatter.format_sentences(tokens)

    # Save output
    utils.save_text(formatted, output_path)

    print(f"Formatted transcript saved at {output_path}")
    print("Preview:\n")
    print(formatted[:500])


if __name__ == "__main__":
    main()
