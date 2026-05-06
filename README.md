# AI-Resume-Screening-System-using-BERT
## Overview
This project is an NLP-based AI Resume Screening System that uses Transformer embeddings and semantic similarity to match resumes with job descriptions.

## Features
- Semantic resume-job matching
- Transformer embeddings using Sentence Transformers
- Match score generation
- Interactive Streamlit UI

## Tech Stack
- Python
- Hugging Face Transformers
- Sentence Transformers
- Streamlit
- PyTorch

## How It Works
1. User enters job description
2. Resume content is processed
3. Embeddings are generated
4. Cosine similarity calculates match score

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
