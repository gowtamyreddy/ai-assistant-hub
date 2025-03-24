import streamlit as st
from PIL import Image
from google import genai

# ✅ Use Streamlit secret for API key
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

# ✅ Page config
st.set_page_config(
    page_title="AI Assistant Hub",
    page_icon="🤖",
    layout="centered"
)

# ✅ Optional logo display
try:
    logo = Image.open("logo.png")  # use your new transparent logo file
    st.image(logo, width=120)
except:
    st.write("")

# ✅ Title and intro
st.markdown(
    """
    <h2 style='text-align: center; margin-top: 0;'>Welcome to <span style="color:#4a6cf7;">AI Assistant Hub</span> 👋</h2>
    <p style='text-align: center; font-size: 1.1rem; color: #444;'>Hi Gowtamy! What would you like to do today?</p>
    """,
    unsafe_allow_html=True
)

# ✅ Style override for cleaner look
st.markdown("""
    <style>
    .stButton > button {
        background-color: #4a6cf7;
        color: white;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        border-radius: 6px;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
        border: none;
    }

    .stButton > button:hover {
        background-color: #3859e0;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Buttons (centered)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

if st.button("🎨 Generate an Image"):
    st.switch_page("pages/image_generator.py")

if st.button("🖼️ Generate an Image Caption"):
    st.switch_page("pages/image_caption.py")

if st.button("📺 Summarize a YouTube Video"):
    st.switch_page("pages/youtube_summary.py")

st.markdown("</div>", unsafe_allow_html=True)

# ✅ Footer
st.markdown("<hr style='margin-top: 2rem;'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 0.85rem; color: #999;'>Crafted with ❤️ by Gowtamy</p>",
    unsafe_allow_html=True
)
