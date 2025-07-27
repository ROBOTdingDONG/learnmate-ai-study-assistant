# 📚 LearnMate - AI Study Assistant

An intelligent study companion that transforms your notes and PDFs into personalized study materials using AI.

## ✨ Features

- **📄 PDF Processing** - Extract text from uploaded PDF documents
- **🔍 Adaptive Summaries** - AI-generated summaries that scale with content length
- **🧠 Smart Flashcards** - Dynamic flashcard generation (3-15 cards based on content)
- **🎯 Quiz Generation** - Adaptive multiple-choice questions (2-10 questions)
- **💬 Interactive Chat** - Ask for specific topics, more questions, or explanations
- **📏 Content Scaling** - Automatically adjusts output based on document length

## 🚀 Live Demo

[**Try LearnMate Live →**](your-deployment-url-here)

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI**: OpenAI GPT-4
- **PDF Processing**: PyMuPDF (fitz)
- **Language**: Python 3.13
- **Deployment**: Streamlit Community Cloud

## 📱 How It Works

1. **Upload** your study material (PDF or text)
2. **Analyze** - LearnMate processes and scales content appropriately
3. **Study** - Get summaries, flashcards, and quiz questions
4. **Chat** - Ask for specific help or additional materials

## 🔧 Content Scaling

| Text Length | Summary Type | Flashcards | Quiz Questions |
|-------------|-------------|------------|----------------|
| < 500 chars | Brief | 3 cards | 2 questions |
| 500-1500 | Moderate | 5 cards | 3 questions |
| 1500-3000 | Detailed | 8 cards | 5 questions |
| 3000-5000 | Comprehensive | 12 cards | 7 questions |
| > 5000 chars | Extensive | 15 cards | 10 questions |

## 💬 Chat Examples

- "Generate 5 more flashcards about photosynthesis"
- "Create harder quiz questions"
- "Explain quantum mechanics in more detail"
- "Make flashcards focusing on definitions"

## 🏃 Local Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with OpenAI API key
4. Run: `streamlit run app.py`

## 📁 Project Structure

```
LearnMate/
├── app.py                 # Main Streamlit application
├── agent_logic.py         # AI logic and OpenAI integration
├── utils/
│   ├── flashcard_gen.py   # Flashcard generation
│   └── pdf_parser.py      # PDF text extraction
├── requirements.txt       # Dependencies
└── .env                   # Environment variables (not in repo)
```

## 🎯 Future Enhancements

- Support for more file formats (Word, PowerPoint)
- Spaced repetition scheduling
- Progress tracking
- Multiple AI model support
- Collaborative study groups

## 👨‍💻 Developer

**[Your Name]** - AI/ML Developer  
[Your Portfolio] | [LinkedIn] | [GitHub]

---

*Built with ❤️ and AI to make studying more efficient and effective.*
