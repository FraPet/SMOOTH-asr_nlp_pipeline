# src/utils.py
import os

def save_text(content, filepath):
    """
    Save text content to a file.
    Creates directories if they do not exist.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
