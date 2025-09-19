# Automatic Speech-to-Text Pipeline

This repository contains the code used in the analyses reported in the paper:

**D’Ortenzio, S., Petriglia, F., Gasparotto, G., Andreetta, S., Gobbo, M., & Marini, A. (under revision). Aging, Cognitive Efficiency, and Lifelong Learning: Impacts on Simple and Complex Sentence Production during storytelling. Brain Sciences.**

---

## Overview
The repository provides a minimal pipeline to convert audio files into text using **Whisper** (OpenAI) for automatic speech recognition (ASR) and **spaCy** for linguistic annotation.  
The pipeline was developed and applied to narrative discourse data in the above-mentioned study, and is made openly available to support reproducibility and methodological transparency.

---

## Features
- End-to-end pipeline: **audio → text**
- Based on [Whisper](https://github.com/openai/whisper) for ASR
- [spaCy](https://spacy.io/) integration for Part-of-Speech tagging
- Option to **preserve original labels** or apply translated/custom label sets
- Ready-to-run **Google Colab notebook** (`notebooks/pipeline_demo.ipynb`)

---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/YOURUSERNAME/asr_pipeline.git
cd asr_pipeline
pip install -r requirements.txt
```

Install the spaCy model (example for Italian):
```bash
python -m spacy download it_core_news_sm
```

---

## Usage
You can either run the pipeline via the provided Colab notebook or import the modules directly.

### Example (Python)
```python
from src import transcription, postprocessing, utils
from src.config import LANGUAGE

# Load Whisper model
model = transcription.load_model("base")

# Transcribe demo audio
text, segments = transcription.transcribe_audio(model, "data/example_audio/demo.wav", language=LANGUAGE)

# Run POS tagging
tokens = postprocessing.process_text(text)

# Save transcript
utils.save_text(text, "data/outputs/demo_transcript.txt")

print(text[:200])
```

---

## Data availability
Due to privacy and ethical restrictions, raw audio and verbatim transcripts from the study cannot be shared.  
We provide demo audio and example transcripts in `data/example_audio/` for illustration purposes.  

---

## Citation
If you use this code, please cite the paper once published:

**D’Ortenzio, S., Petriglia, F., Gasparotto, G., Andreetta, S., Gobbo, M., & Marini, A. (under revision). Aging, Cognitive Efficiency, and Lifelong Learning: Impacts on Simple and Complex Sentence Production during storytelling. Brain Sciences.**

And also cite the software dependencies:
- Radford et al., 2022 (Whisper)
- Honnibal et al., 2020 (spaCy)