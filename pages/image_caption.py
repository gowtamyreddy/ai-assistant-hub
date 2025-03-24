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

st.title("Caption Generator")
uploaded_img = st.file_uploader("Generating the caption of the img")

if uploaded_img:
    image = Image.open(uploaded_img)
    st.image(image,caption = "Uploaded imgage")

    if st.button("Generate Caption"):
        try:
            with st.spinner("Generating Image Capion ..."):

                response = client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=["What is this image?",image])
                st.subheader("Generated Caption ")   
                st.write(response.text)

        except Exception as e:
            st.error('Error in generating caption')
