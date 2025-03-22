# Crohn Compass: Voice-Powered Chat for Navigating Crohn's Disease

> **Proof-of-Concept** | AI-powered chat built for clarity, empathy, and scientific grounding

---

## 🚀 Problem
Crohn's patients face a complex, often overwhelming landscape: conflicting information, inconsistent advice, and a steep learning curve. Especially for those newly diagnosed or still seeking answers, understanding the disease — and acting on reliable guidance — can feel impossible.

---

## 🧐 Hypothesis
A conversational, voice-first assistant — tuned to speak plainly but backed by science — can radically improve how Crohn-interested users access, absorb, and act on relevant knowledge. When friction to understanding drops, confidence and outcomes rise.

---

## ⚙️ What It Does
**Crohn Compass** is a voice-to-chat interface that:

- Listens to the user via speech (voice-to-text)
- Delivers friendly, digestible, age-15-level explanations
- Surfaces deeper, evidence-based studies when asked
- Covers:
  - What Crohn's disease is
  - Symptoms and red flags
  - Treatment paths
  - Good/bad food habits
  - Lifestyle guidance
  - When to seek professional care

---

## 🎓 Who It's For
- Newly diagnosed patients
- Long-term sufferers wanting more clarity
- Individuals experiencing symptoms but undiagnosed

This is *not* a diagnostic tool — it's an educational companion.

---

## ⚡ Tech Stack
| Layer | Tech |
|------|------|
| UI | Streamlit |
| Voice-to-Text | SpeechRecognition (Google Speech API) |
| LLM | OpenAI (GPT-4) |
| Language | Python |

The stack was chosen for fast iteration and natural UX:
- **Streamlit**: dead-simple UI, real-time interactivity
- **SpeechRecognition**: reliable speech-to-text conversion
- **OpenAI**: powerful LLM with healthcare knowledge

---

## 🔮 What's Interesting Here
- **Voice-native UX**: Designed for accessibility and low-friction interaction
- **Conversational layering**: Friendly by default, scientific on demand
- **Prompt scaffolding**: Uses few-shot examples to maintain tone + fact depth

---

## 🔢 How to Run Locally

### Prerequisites
- Python 3.8 or higher
- An OpenAI API key

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crohn-compass.git
   cd crohn-compass
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

6. Open your browser and navigate to the URL displayed in the terminal (usually http://localhost:8501)

### Usage

1. Use the "Speak to Crohn Compass" button to ask questions with your voice
2. Alternatively, type your questions in the text input field
3. Click on the suggested topics to get started with common questions
4. Use the "Clear Chat" button to reset the conversation

---

## 📊 Next Experiments
- ✏️ Fine-tune voice output for more empathetic tone
- 🪨 Add retrieval-augmented generation (RAG) for citing latest studies
- ⚛️ Offline mode using Whisper + local LLMs

---

## 🚫 Disclaimer
This is not medical advice. Always consult a licensed physician for diagnosis and treatment.

---

## 📅 Project Status
> ✅ **Prototype complete** — voice input working, LLM integration live.
> ⌛ **Next step** — deploy for feedback from actual users in the Crohn's community.

---

## 🌍 License
MIT License — open for contribution, adaptation, and iteration.

---

## 🚀 Why This Matters
Crohn's is hard enough. Understanding it shouldn't be. This project is a bet on clarity, empathy, and accessible science — powered by AI, delivered like a human would explain to a friend.

---

