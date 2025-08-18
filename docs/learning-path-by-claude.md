# AI Learning Plan for Generative AI & Practical Applications

Tailored for Software Developer with Java/Kotlin Background

## 🎯 Goals

- Quick practical application of generative AI
- Portfolio projects on GitHub/HuggingFace
- English learning app as main project
- Use and fine-tune existing models

## 📅 Timeline
12 Weeks (1-2h daily)

## Phase 1: Fundamentals & Python Setup (Weeks 1-2)

### Week 1: Preparing Python for AI

Platforms: edX + Independent Learning

- Main Course: [Python for Everybody - edX (MichiganX)](https://learning.edx.org/course/course-v1:MichiganX+py4e101x+2T2024/home) - structured course with videos and exercises
- Supplementary: [PY4E - Python for Everybody](https://www.py4e.com/) (additional materials and reference)
- Focus: Python syntax, lists, dictionaries, functions, file handling
- Hands-on:
    - Set up Python environment (Anaconda/Miniconda)
    - Learn Jupyter Notebooks
    - First small Python project: [Read and analyze vocabulary file](learnings/hands-on/week1/README.md)

### Week 2: Data Science Libraries Basics

Platforms: Independent + HuggingFace Docs

- Learning Goal: pandas, numpy, matplotlib fundamentals
- Resources:
  - [Python Data Science Handbook (free online)](https://jakevdp.github.io/PythonDataScienceHandbook/)
  - [pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)

- Hands-on:
  - Create first HuggingFace account and explore HuggingFace Docs: already have a [HuggingFace account](https://huggingface.co/jacq-42)
  - [Read and manipulate CSV files and visualize data](learnings/hands-on/week2/README.md)

## Phase 2: AI Fundamentals & First Models (Weeks 3-5)

### Week 3: Machine Learning Overview

Platform: fast.ai

- Course: [Practical Deep Learning for Coders](https://course.fast.ai/) - Lesson 1-2
- Focus: What is ML/DL, transfer learning, first models
- Hands-on:
  - First image classification model with fast.ai
  - Understand concepts: Training, validation, overfitting

### Week 4: NLP Fundamentals

Platforms: HuggingFace + DeepLearning.AI

- HuggingFace: [NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1) (Chapters 1-3)
- Focus: Tokenization, Transformers, BERT fundamentals
- Hands-on:
  - Text classification with pretrained model
  - Implement sentiment analysis example
  - Create first repository on HuggingFace

### Week 5: Generative AI Introduction

Platform: DeepLearning.AI

- Course: [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) (free)
- Focus: Understanding GPT models, prompt engineering
- Hands-on:
  - OpenAI API or HuggingFace Transformers for text generation
  - Simple chatbot prototype
  - Test various prompting strategies

## Phase 3: Audio & Multimodal AI (Weeks 6-7)

### Week 6: Speech-to-Text & Text-to-Speech

Platforms: HuggingFace + Independent

- Resources:
  - [HuggingFace Audio Course](https://huggingface.co/learn/audio-course/chapter0/introduction)
  - [OpenAI Whisper Documentation](https://platform.openai.com/docs/guides/speech-to-text)
  - [HuggingFace Audio Tasks](https://huggingface.co/tasks/automatic-speech-recognition)
- Focus: ASR (Automatic Speech Recognition), TTS models
- Hands-on:
  - Implement Whisper for transcription
  - Text-to-Speech with HuggingFace models
  - Process audio files (librosa library)

### Week 7: Multimodal Models

Platforms: HuggingFace + Papers

- Focus: Vision-language models, audio-text combination
- Hands-on:
  - Image-to-text generation
  - Combine audio + text processing
  - Preparation for main project

## Phase 4: Main Project - English Learning App (Weeks 8-12)

### Week 8: Project Planning & Architecture

- Finalize app concept:
  - Vocabulary management system
  - Grammar rule engine
  - Chat interface design
  - Audio integration planning

- Define tech stack:
  - Backend: Python (FastAPI/Flask)
  - Frontend: React/Vue or Streamlit for MVP
  - AI: HuggingFace Transformers + OpenAI API
  - Database: SQLite for start

### Week 9: Backend & AI Integration

- Develop components:
  - Chat-bot with GPT/Claude for conversation
  - Vocabulary context system (RAG with vector database)
  - Grammar feedback system
  - Audio transcription pipeline (Whisper)

### Week 10: Frontend & User Experience

- Develop interface:
  - Chat interface
  - Vocabulary input/management
  - Audio recording and playback
  - Progress tracking

### Week 11: Advanced Features

- Expand AI features:
  - Personalized feedback based on errors
  - Adaptive difficulty levels
  - Spaced repetition for vocabulary
  - Pronunciation assessment

### Week 12: Deployment & Portfolio

- Finalization:
  - App deployment (Streamlit Cloud/Heroku)
  - HuggingFace Spaces demo
  - Document GitHub repository
  - Create portfolio presentation