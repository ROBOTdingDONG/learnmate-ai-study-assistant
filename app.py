import streamlit as st
from utils.flashcard_gen import generate_flashcards
from agent_logic import ask_ai
from utils.pdf_parser import extract_text_from_pdf
import tempfile
import os

st.title("📚 LearnMate - AI Study Assistant")

# Check if API key is set
if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "your_new_openai_key_here":
    st.error("⚠️ Please set your OPENAI_API_KEY in the .env file!")
    st.stop()

# Initialize session state for chat and extracted text
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to determine content scale based on text length
def get_content_scale(text_length):
    if text_length < 500:
        return {"summary_detail": "brief", "flashcards": 3, "quiz_questions": 2}
    elif text_length < 1500:
        return {"summary_detail": "moderate", "flashcards": 5, "quiz_questions": 3}
    elif text_length < 3000:
        return {"summary_detail": "detailed", "flashcards": 8, "quiz_questions": 5}
    elif text_length < 5000:
        return {"summary_detail": "comprehensive", "flashcards": 12, "quiz_questions": 7}
    else:
        return {"summary_detail": "extensive", "flashcards": 15, "quiz_questions": 10}

# Function to generate adaptive flashcards
def generate_adaptive_flashcards(text, num_cards):
    prompt = f"Convert the following text into {num_cards} flashcards in Q&A format. Make sure to cover the most important concepts:\n\n{text}"
    return ask_ai(prompt)

uploaded_file = st.file_uploader("Upload your PDF notes", type="pdf")
custom_input = st.text_area("Or paste your notes directly:")

if st.button("📊 Analyze & Generate Study Materials"):
    text = ""
    
    # Show processing message
    with st.spinner("Processing..."):
        try:
            if uploaded_file:
                st.info("📄 Processing PDF file...")
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                
                # Extract text after file is closed
                text = extract_text_from_pdf(tmp_path)
                
                # Clean up temp file
                try:
                    os.unlink(tmp_path)
                except:
                    pass  # Ignore cleanup errors
                    
                st.success(f"✅ Extracted {len(text)} characters from PDF")
                
            elif custom_input:
                text = custom_input
                st.success("✅ Text input received")
            else:
                st.warning("⚠️ Please upload a PDF or enter text to analyze!")
                st.stop()

            if text.strip():
                # Store text in session state for chat
                st.session_state.extracted_text = text
                
                # Determine content scale
                scale = get_content_scale(len(text))
                st.info(f"📏 Text length: {len(text)} characters | Content scale: {scale['summary_detail']}")
                
                # Adaptive Summary
                st.subheader("🔍 Summary")
                try:
                    if scale['summary_detail'] == "brief":
                        summary_prompt = f"Provide a brief summary (2-3 sentences) of:\n\n{text}"
                    elif scale['summary_detail'] == "moderate":
                        summary_prompt = f"Provide a moderate summary (1 paragraph) of:\n\n{text}"
                    elif scale['summary_detail'] == "detailed":
                        summary_prompt = f"Provide a detailed summary (2-3 paragraphs) covering main points:\n\n{text}"
                    elif scale['summary_detail'] == "comprehensive":
                        summary_prompt = f"Provide a comprehensive summary (3-4 paragraphs) with key details:\n\n{text}"
                    else:  # extensive
                        summary_prompt = f"Provide an extensive summary (4-5 paragraphs) covering all important aspects:\n\n{text}"
                    
                    summary = ask_ai(summary_prompt)
                    st.write(summary)
                except Exception as e:
                    st.error(f"❌ Error generating summary: {str(e)}")

                # Adaptive Flashcards
                st.subheader(f"🧠 Flashcards ({scale['flashcards']} cards)")
                try:
                    flashcards = generate_adaptive_flashcards(text, scale['flashcards'])
                    st.write(flashcards)
                except Exception as e:
                    st.error(f"❌ Error generating flashcards: {str(e)}")

                # Adaptive Quiz Questions
                st.subheader(f"🎯 Quiz Questions ({scale['quiz_questions']} questions)")
                try:
                    quiz = ask_ai(f"Generate {scale['quiz_questions']} multiple-choice questions with 4 options each and indicate the correct answer. Cover the most important concepts from:\n\n{text}")
                    st.write(quiz)
                except Exception as e:
                    st.error(f"❌ Error generating quiz: {str(e)}")
            else:
                st.warning("⚠️ No text found to process!")
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.write("Please check your API keys and try again.")

# Chat Interface
st.markdown("---")
st.subheader("💬 Chat with LearnMate")

# Only show chat if we have extracted text
if st.session_state.extracted_text:
    st.write("Ask me to generate more flashcards, quiz questions, explain specific topics, or anything else about your study material!")
    
    # Display chat history
    for i, (user_msg, bot_msg) in enumerate(st.session_state.chat_history):
        st.write(f"**You:** {user_msg}")
        st.write(f"**LearnMate:** {bot_msg}")
        st.markdown("---")
    
    # Chat input
    user_question = st.text_input("Ask LearnMate anything about your study material:", key="chat_input")
    
    if st.button("Send") and user_question:
        with st.spinner("Thinking..."):
            try:
                # Enhanced prompt that includes the extracted text for context
                chat_prompt = f"""You are LearnMate, an AI study assistant. Based on the following study material, answer the user's question:

STUDY MATERIAL:
{st.session_state.extracted_text[:2000]}...

USER QUESTION: {user_question}

If the user asks for more flashcards, quiz questions, or explanations about specific topics, generate them based on the study material above. Be helpful and educational."""

                bot_response = ask_ai(chat_prompt)
                
                # Add to chat history
                st.session_state.chat_history.append((user_question, bot_response))
                
                # Rerun to update display
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error in chat: {str(e)}")
    
    # Clear chat history button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
        
else:
    st.info("👆 Please analyze some study material first to start chatting!")

# Examples of what users can ask
with st.expander("💡 Example Chat Commands"):
    st.write("""
    - "Generate 5 more flashcards about [specific topic]"
    - "Create harder quiz questions"
    - "Explain [concept] in more detail"
    - "Make flashcards focusing on definitions"
    - "Generate true/false questions"
    - "What are the key takeaways?"
    - "Create a study plan for this material"
    """)