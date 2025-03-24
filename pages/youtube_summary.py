import streamlit as st
from google import genai
from google.genai import types

# ✅ Use API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]

# ✅ Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

# ✅ UI
st.title("📺 AI Video Summarizer")
st.markdown("Paste a YouTube video URL below to get a smart AI-generated summary.")

youtube_url = st.text_input("🔗 Enter the YouTube video URL")

if st.button("Summarize the Video"):
    if not youtube_url:
        st.warning("🚨 Please enter a video URL first.")
    else:
        try:
            with st.spinner("⏳ Summarizing..."):
                response = client.models.generate_content(
                    model="models/gemini-2.0-flash",
                    contents=types.Content(
                        parts=[
                            types.Part(text="Can you summarize this video?"),
                            types.Part(file_data=types.FileData(file_uri=youtube_url))
                        ]
                    )
                )
            st.subheader("📝 Video Summary")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
