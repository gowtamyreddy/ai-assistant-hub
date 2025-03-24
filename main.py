import streamlit as st
from PIL import Image
from google import genai

# ✅ API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

# ✅ Page config
st.set_page_config(
    page_title="AI Assistant Hub",
    page_icon="🤖",
    layout="centered"
)

# ✅ Optional logo
try:
    logo = Image.open("logo.png")  # or logo-transparent.png
    st.image(logo, width=120)
except:
    st.write("")

# ✅ Title & intro
st.markdown(
    """
    <h2 style='text-align: center;'>Welcome to <span style="color:#3b5bdb;">AI Assistant Hub</span> 👋</h2>
    <p style='text-align: center; font-size: 1.1rem; color: #444;'>Hi Gowtamy! What would you like to do today?</p>
    """,
    unsafe_allow_html=True
)

# ✅ Custom styling for consistent buttons
st.markdown("""
    <style>
    .custom-button button {
        background-color: #3b5bdb;
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        width: 300px;
        margin: 0.5rem auto;
        display: block;
        text-align: center;
        transition: background-color 0.2s ease;
    }

    .custom-button button:hover {
        background-color: #2f4ab9;
        color: white;
    }

    .footer-text {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #aaa;
    }

    hr {
        border: none;
        border-top: 1px solid #eee;
        margin-top: 2rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Buttons with uniform style
st.markdown('<div class="custom-button">', unsafe_allow_html=True)

if st.button("🎨 Generate an Image", key="image"):
    st.switch_page("pages/image_generator.py")

if st.button("🖼️ Generate an Image Caption", key="caption"):
    st.switch_page("pages/image_caption.py")

if st.button("📺 Summarize a YouTube Video", key="summary"):
    st.switch_page("pages/youtube_summary.py")

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer-text'>Crafted with ❤️ by Gowtamy</div>", unsafe_allow_html=True)
