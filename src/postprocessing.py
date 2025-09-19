# src/postprocessing.py
import spacy
from .config import (
    LANGUAGE, KEEP_ORIGINAL_LABELS,
    SPACY_MODEL_IT, SPACY_MODEL_EN,
    LABEL_MAPPING_IT, PREPOSITION_MAPPING,
    LIST_ANQ, LIST_CONG_ALL, GENERIC_MAPPING
)

# Load spaCy models
nlp_it = spacy.load(SPACY_MODEL_IT)
nlp_en = spacy.load(SPACY_MODEL_EN)


def map_label_it(token, next_token=None):
    """
    Apply Italian-specific mapping rules to a token.
    Returns a list of (word, label) pairs.
    """
    word = token.text.lower()

    # Prepositional contractions (e.g., "della" -> de/Prep + +lla/Art)
    if word in PREPOSITION_MAPPING:
        c1, c2 = PREPOSITION_MAPPING[word]
        return [(c1, "PREP"), (c2, "ART")]

    # Demonstratives/anaphorics
    if word in LIST_ANQ:
        return [(word, "ANQ")]

    # Adversative conjunctions
    if word in LIST_CONG_ALL:
        return [(word, "CONG_ALL")]

    # Fillers and generic mapping
    if word in GENERIC_MAPPING:
        return [(word, GENERIC_MAPPING[word])]

    # Auxiliary vs. main verb
    if token.pos_ == "AUX":
        if next_token is not None and next_token.pos_ != "VERB":
            return [(word, "VERBO")]
        return [(word, "AUX")]

    # Default mapping
    if token.pos_ in LABEL_MAPPING_IT:
        return [(word, LABEL_MAPPING_IT[token.pos_])]

    # Fallback: raw spaCy POS
    return [(word, token.pos_.upper())]


def process_text(text, language=LANGUAGE):
    """
    Process a text string and return a list of (word, label) pairs.
    - For Italian: applies custom mapping rules
    - For English: returns raw spaCy POS or token.pos_
    """
    nlp = nlp_it if language == "it" else nlp_en
    doc = nlp(text)

    tokens_out = []
    for i, token in enumerate(doc):
        if token.pos_ in ["SPACE"]:
            continue
        if token.pos_ == "PUNCT":
            tokens_out.append(("<END>", "SENT_END"))
            continue

        next_token = doc[i+1] if i+1 < len(doc) else None

        if language == "it":
            mapped = map_label_it(token, next_token)
            tokens_out.extend(mapped)
        else:  # English or other language
            if KEEP_ORIGINAL_LABELS:
                tokens_out.append((token.text.lower(), token.pos_))
            else:
                tokens_out.append((token.text.lower(), token.tag_))
    return tokens_out
