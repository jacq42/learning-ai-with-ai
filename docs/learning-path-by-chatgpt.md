# 📅 4-Month AI Learning & Project Plan (100% Free)

- Goal: Build functional AI applications, understand the models, and deploy them online.
- Time commitment: 1–2 hours/day → ~7–10 hours/week.

## Phase 1 – Foundations & Setup (Weeks 1–4)

Focus: AI & Python basics + small ML models

| Week | Course / Material                                                                                                               | Tools & Exercises                                                | Mini Project                                                 |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| 1    | 🎥 [Introduction to Artificial Intelligence (freeCodeCamp, 2h)](https://www.youtube.com/watch?v=JMUxmLyrhSk)                    | Python setup (`conda` or `pip`), `numpy`, `pandas`, `matplotlib` | Data analysis on English vocabulary dataset                  |
| 2    | 🎥 [Python Data Science Crash Course – FreeCodeCamp](https://www.youtube.com/watch?v=LHBE6Q9XlzI)                               | `scikit-learn` basics                                            | Small quiz generator from a vocab list                       |
| 3    | 🎥 [Intro to Machine Learning – Kaggle Learn](https://www.kaggle.com/learn/intro-to-machine-learning)                           | Train & evaluate text classification model                       | Grammar rule classifier (simple rule-based or keyword-based) |
| 4    | 📄 [scikit-learn Text Processing Tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) | GitHub repo setup                                                | Upload first NLP experiments                                 |

## Phase 2 – NLP Core Skills (Weeks 5–8)

Focus: Building text models + first chatbot logic

| Week | Course / Material                                                                                                    | Tools & Exercises              | Mini Project                                    |
| ---- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------- |
| 5    | 📄 [Hugging Face NLP Course – Chapters 1–3](https://huggingface.co/course/)                                          | `transformers`, `datasets`     | Vocabulary flashcard generator                  |
| 6    | Hugging Face: [Text Classification Tutorial](https://huggingface.co/docs/transformers/tasks/sequence_classification) | Fine-tuning a small model      | Grammar error detection prototype               |
| 7    | [Gradio Get Started](https://gradio.app/get_started/)                                                                | Build chatbot UI in Gradio     | First rule-based chatbot for English practice   |
| 8    | Hugging Face: [Conversational AI](https://huggingface.co/docs/transformers/tasks/conversational)                     | Integrate conversational model | Chatbot v1 – text only, vocab & grammar prompts |

## Phase 3 – Adding Feedback & Speech-to-Text (Weeks 9–12)

Focus: Interactive English practice + audio input

| Week | Course / Material                                                                                                                                                                 | Tools & Exercises               | Mini Project                               |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------ |
| 9    | Hugging Face: [Token Classification (NER)](https://huggingface.co/docs/transformers/tasks/token_classification)                                                                   | Highlight grammar/vocab usage   | Grammar/vocab feedback module              |
| 10   | [OpenAI Whisper (speech recognition)](https://github.com/openai/whisper) or [Hugging Face Speech Models](https://huggingface.co/models?pipeline_tag=automatic-speech-recognition) | Speech-to-text processing       | Audio transcription from microphone        |
| 11   | Integrate transcription into chatbot                                                                                                                                              | Combine speech → text → chatbot | Audio-enabled chatbot prototype            |
| 12   | Deployment on [Hugging Face Spaces](https://huggingface.co/spaces)                                                                                                                | Live demo                       | Chatbot v2 – text + speech input, feedback |

## Phase 4 – Portfolio & Enhancement (Weeks 13–16)

Focus: Polishing the chatbot + adding advanced features

| Week | Course / Material                            | Tools & Exercises             | Mini Project                           |
| ---- | -------------------------------------------- | ----------------------------- | -------------------------------------- |
| 13   | Add spaced repetition logic (SRS) for vocab  | Store progress                | Adaptive vocabulary trainer            |
| 14   | Add grammar explanations from knowledge base | Retrieve info                 | Explain grammar mistakes automatically |
| 15   | UI/UX improvements (Gradio/Streamlit)        | Polish interface              | Final chatbot version                  |
| 16   | Portfolio finalization                       | README, video demo, blog post | Publish as flagship project            |


## 💡 Tech Stack for the Chatbot

- Model: Hugging Face Transformers (DistilBERT for text classification, DialoGPT or BlenderBot for conversation)
- Feedback: Token classification + custom rules for grammar/vocab detection
- Speech: Whisper (local or via Hugging Face pipeline)
- Frontend: Gradio app deployed on Hugging Face Spaces