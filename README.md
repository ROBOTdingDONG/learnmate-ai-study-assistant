# 📚 LearnMate – AI Study Assistant

A lightweight, Streamlit-based AI chatbot that helps students study smarter by summarizing notes, generating flashcards, and creating quiz questions using GPT-4o.

---

## 🚀 Features

- 🧾 Upload PDFs or paste study notes
- 🧠 Generates flashcards in Q&A format
- 🎯 Auto-generates practice quiz questions
- 🔍 Summarizes complex material into digestible insights
- 🛠️ Built with GPT-4o + Python + Streamlit

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/learnmate-ai-study-assistant.git
cd learnmate-ai-study-assistant
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API Key
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=sk-xxxxxxx
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```
Then open the local server URL provided in your browser.

---

## 📁 Project Structure
```
learnmate-ai-study-assistant/
├── app.py
├── agent_logic.py
├── requirements.txt
├── .env
├── utils/
│   ├── flashcard_gen.py
│   └── pdf_parser.py
```

---

## 📸 Screenshots
> _Add screenshots of your Streamlit interface here_

---

## 🔧 Dependencies
- OpenAI (GPT-4o)
- Streamlit
- python-dotenv
- PyMuPDF (PDF parser)

---

## ✨ Future Features
- Notion integration
- Flashcard export (CSV / Anki)
- Scoring system for quizzes
- Dark mode toggle

---

## 👨‍💻 Author
**Wendell Powell** – [@ROBOTdingDONG](https://github.com/ROBOTdingDONG) • Founder of [Simply AI Solutions](https://simplyaisolutions.co)

---

## 📄 License
MIT License
