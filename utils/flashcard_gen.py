from agent_logic import ask_ai

def generate_flashcards(text):
    prompt = f"Convert the following text into 5 flashcards in Q&A format:\n\n{text}"
    return ask_ai(prompt)