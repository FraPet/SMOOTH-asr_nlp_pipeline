import os

# === Base directories ===
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# === Options ===
KEEP_ORIGINAL_LABELS = True   # If True, keep spaCy POS tags directly
LANGUAGE = "it"               # "it" for Italian pipeline, "en" for English pipeline

# === spaCy models ===
SPACY_MODEL_IT = "it_core_news_lg"
SPACY_MODEL_EN = "en_core_web_sm"

# === POS → Custom label mapping (Italian only) ===
LABEL_MAPPING_IT = {
    "VERB": "VERBO",
    "DET": "ART",
    "NOUN": "NOME",
    "SCONJ": "CONG_ALL",
    "CCONJ": "CONG_E",
    "ADP": "PREP",
    "ADV": "AVV",
    "ADJ": "AGG",
    "PROPN": "NOME",
}

# Prepositional contractions (Italian)
PREPOSITION_MAPPING = {
    "col": ("co", "+l"),
    "del": ("de", "+l"), "dello": ("de", "+llo"), "della": ("de", "+lla"),
    "dei": ("de", "+i"), "degli": ("de", "+gli"), "delle": ("de", "+lle"), "dell'": ("de", "+ll'"),
    "al": ("a", "+l"), "allo": ("a", "+llo"), "alla": ("a", "+lla"), "all'": ("a", "+ll'"),
    "ai": ("a", "+i"), "agli": ("a", "+gli"), "alle": ("a", "+lle"),
    "dal": ("da", "+l"), "dallo": ("da", "+llo"), "dalla": ("da", "+lla"),
    "dai": ("da", "+i"), "dagli": ("da", "+gli"), "dalle": ("da", "+lle"), "dall'": ("da", "+ll'"),
    "nel": ("ne", "+l"), "nello": ("ne", "+llo"), "nella": ("ne", "+lla"),
    "nei": ("ne", "+i"), "negli": ("ne", "+gli"), "nelle": ("ne", "+lle"), "nell'": ("ne", "+ll'"),
    "sul": ("su", "+l"), "sullo": ("su", "+llo"), "sulla": ("su", "+lla"),
    "sui": ("su", "+i"), "sugli": ("su", "+gli"), "sulle": ("su", "+lle"), "sull'": ("su", "+ll'"),
}

# Demonstratives / anaphorics
LIST_ANQ = [
    "questo", "questa", "quello", "quella", "quest'",
    "questi", "queste", "quelli", "quelle",
    "mio", "mia", "tuo", "tua", "suo", "sua",
    "miei", "mie", "tuoi", "tue", "suoi", "sue",
    "altro", "altra", "altre", "altri"
]

# Adversative and coordinating conjunctions
LIST_CONG_ALL = ["però", "ma", "mentre", "o", "quindi", "perché"]

# Generic filler mapping (Italian)
GENERIC_MAPPING = {
    "immagine": "FILLER", "vignetta": "FILLER", "vignette": "FILLER",
    "scena": "FILLER", "scenetta": "FILLER", "appunto": "FILLER",
    "probabilmente": "FILLER", "insomma": "FILLER", "praticamente": "FILLER",
    "presumibilmente": "FILLER", "chiaramente": "FILLER", "ovviamente": "FILLER",
    "diciamo": "FILLER", "immagino": "FILLER", "suppongo": "FILLER",
    "contro": "PREP", "verso": "PREP", "dentro": "PREP",
}
