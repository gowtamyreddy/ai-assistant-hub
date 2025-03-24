import streamlit as st
from PIL import Image
from google import genai

# ✅ Use API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

# ✅ Must be first!
st.set_page_config(
    page_title="AI Assistant Hub",
    page_icon="🤖",
    layout="centered"
)

# ✅ Hide Streamlit command bar + footer
st.markdown("""
    <style>
    header[data-testid="stHeader"] {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Custom styling for fonts, layout, buttons, sidebar
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f9fafc;
    }

    .main-container {
        background-color: #ffffff;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        max-width: 600px;
        margin: 4rem auto;
        text-align: center;
    }

    h1 {
        font-size: 2.25rem;
        color: #222;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    h4 {
        font-weight: 400;
        color: #555;
        margin-bottom: 2rem;
    }

    .stButton > button {
        width: 100%;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        background-color: #4a6cf7;
        color: white;
        border: none;
        border-radius: 8px;
        margin-bottom: 1rem;
        transition: background-color 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #3859e0;
    }

    .footer-text {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #999;
    }

    section[data-testid="stSidebar"] {
        background-color: #f0f2f6;
        padding-top: 2rem;
    }

    .css-1d391kg, .css-1v0mbdj, .css-1dp5vir {
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        color: #333 !important;
    }

    .css-1v0mbdj {
        background-color: #e0e7ff !important;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Main container layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ✅ Display Logo
try:
    logo = Image.open("logo.png")
    st.image(logo, width=120)
except:
    st.warning("Logo not found. Please ensure 'logo.png' is in your project directory.")

st.markdown("<h1>Welcome to AI Assistant Hub 👋</h1>", unsafe_allow_html=True)
st.markdown("<h4>Hi Gowtamy! What would you like to do today?</h4>", unsafe_allow_html=True)

if st.button("🎨 Generate an Image"):
    st.switch_page("pages/image_generator.py")

if st.button("🖼️ Generate an Image Caption"):
    st.switch_page("pages/image_caption.py")

if st.button("📺 Summarize a YouTube Video"):
    st.switch_page("pages/youtube_summary.py")

st.markdown("</div>", unsafe_allow_html=True)

# ✅ Footer
st.markdown('<div class="footer-text">Crafted by Gowtamy</div>', unsafe_allow_html=True)
