# Deployment Instructions

## Method 1: Streamlit Community Cloud (Recommended)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - LearnMate AI Study Assistant"
   git branch -M main
   git remote add origin https://github.com/yourusername/learnmate.git
   git push -u origin main
   ```

2. **Deploy on Streamlit:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Set main file: `app.py`
   - Add secrets for OPENAI_API_KEY

3. **Environment Variables:**
   - In Streamlit Cloud settings, add your API key as a secret
   - Don't include the actual .env file in your repo

## Method 2: Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Choose Streamlit as the SDK
3. Upload your files
4. Add API key in Space settings

## Method 3: Railway

1. Connect your GitHub repo to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically

## Important Notes

- Never commit your .env file with real API keys
- Use secrets/environment variables in production
- Test your deployment before sharing
- Update your README with the live demo link
