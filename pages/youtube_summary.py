import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Client
client = genai.Client(api_key=API_KEY)

st.title("AI Video Summarizer")
youtube_url = st.text_input("Enter the vedio url")

if st.button("Summarize the vedio"):
    if not youtube_url:
        st.warning("Please enter the url")
    
    else:
        try:
            with st.spinner("Generating the summary ...."):

                response = client.models.generate_content(
                model='models/gemini-2.0-flash',
                contents=types.Content(
                    parts=[
                        types.Part(text='Can you summarize this video?'),
                        types.Part(
                            file_data=types.FileData(file_uri=youtube_url)
                        )
                    ]
                )
                )
            st.subheader("Vedio Sumarry")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")