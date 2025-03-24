import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ✅ Use API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]

# Initialize Client
client = genai.Client(api_key=API_KEY)

# Streamlit UI
st.title("AI Image Generator")

prompt = st.text_input("Enter your image prompt")

if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Generating image..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["Text", "Image"]
                    )
                )

                st.subheader("🔍 Result")
                for part in response.candidates[0].content.parts:
                    if part.text:
                        st.write(part.text)
                    elif part.inline_data:
                        image = Image.open(BytesIO(part.inline_data.data))
                        st.image(image, caption="Generated Image")
        except Exception as e:
            st.error(f"❌ Error: {e}")
