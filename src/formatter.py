# src/formatter.py

def format_sentences(tokens):
    """
    Format tokens into CHAT-like lines with *PAR:
    Each sentence starts with '*PAR:\t' followed by word/LABEL pairs.
    Sentence boundaries are determined by the 'SENT_END' marker.
    """
    output_lines = []
    sentence = "*PAR:\t"

    for word, label in tokens:
        if label == "SENT_END":
            if sentence.strip() != "*PAR:":
                output_lines.append(sentence.strip())
            sentence = "*PAR:\t"
        else:
            sentence += f"{word}/{label} "

    # Handle last sentence (if not empty)
    if sentence.strip() != "*PAR:":
        output_lines.append(sentence.strip())

    return "\n".join(output_lines)
