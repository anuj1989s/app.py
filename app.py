import streamlit as st
import time
import random

# Page config for better look
st.set_page_config(
    page_title="Anuj's AI Ad Video Maker",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for nice look (dark mode friendly)
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    .stButton>button {background-color: #00d4ff; color: black; font-weight: bold; border-radius: 8px; padding: 12px 24px;}
    .stTextArea>div>div>textarea {background-color: #1e1e2e; color: white; border-radius: 8px;}
    .stSlider>div>div>div {background-color: #00d4ff;}
    h1, h2, h3 {color: #00d4ff;}
    .stSuccess {background-color: #1e3a2f; color: #d4ff00;}
    </style>
""", unsafe_allow_html=True)

# Sidebar for extra settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.info("Bhai, yeh tera personal tool hai – future mein yahan API keys, voice style etc add kar lenge")
    groq_key = st.text_input("Groq API Key (optional abhi)", type="password", value="")
    st.markdown("---")
    st.caption("Made with ❤️ by Anuj Bhai (Bhopal)")

# Main content
st.title("🎬 Anuj's AI Video Ad Maker")
st.subheader("Prompt daal → Scene-by-scene Ad Video with Auto Audio!")

col1, col2 = st.columns([3, 1])

with col1:
    prompt = st.text_area(
        "Apna Product Ad Prompt Daal (Hindi ya English mein likh sakta hai)",
        height=180,
        placeholder="Example: Ek premium black wireless earbuds ka 30 second energetic ad banao. Young ladka park mein running karta hua, sweat-free feel, powerful bass sound highlight, price only ₹1999, last mein 'Abhi order karo!' text with call-to-action button.",
        key="prompt_input"
    )

with col2:
    duration = st.slider("Video Kitne Second Ka?", 15, 90, 30, step=5)
    language = st.selectbox("Voice Language", ["Hindi (hi)", "English (en)"], index=0)
    lang_code = "hi" if language.startswith("Hindi") else "en"

if st.button("🚀 Video Generate Karo!", type="primary", use_container_width=True):
    if not prompt.strip():
        st.error("Bhai prompt toh daal de pehle! 😅")
    else:
        with st.spinner("AI soch raha hai... scenes break kar raha, script likh raha..."):
            time.sleep(2.5)  # fake delay for now
            
            st.subheader("Step 1: Generated Script & Scenes (Placeholder)")
            st.info("Yahan real mein LLM se aayega scene-by-scene breakdown + narration text")
            
            # Fake output dikha rahe hain taaki frontend accha lage
            fake_script = f"""
Scene 1 (0-8 sec): {prompt.split('.')[0] or 'Product intro'}
Narration: "Dosto, taiyar ho jao naye sound ke liye!"

Scene 2 (8-18 sec): Action scene – runner using earbuds
Narration: "Powerful bass aur crystal clear sound, workout ke time bhi perfect fit!"

Scene 3 (18-25 sec): Close-up + features
Narration: "Sweat-proof, 40 hours battery, sirf ₹1999 mein!"

Scene 4 (25-{duration} sec): Call to action
Narration: "Abhi order karo aur apna game badhao!"
"""
            st.code(fake_script, language="markdown")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent in range(0, 101, 5):
            time.sleep(0.4 if percent > 70 else 0.2)
            progress_bar.progress(percent)
            if percent < 30:
                status_text.text("Scenes create ho rahe hain...")
            elif percent < 60:
                status_text.text("Audio narration ban raha hai...")
            elif percent < 85:
                status_text.text("Visuals + transitions add ho rahe...")
            else:
                status_text.text("Final rendering... almost done!")
        
        status_text.success("✅ Video taiyar hai! (Abhi placeholder – real mein .mp4 download milega)")
        
        # Fake video player
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # sample video – baad mein real replace
        st.download_button("⬇️ Video Download Karo", data=b"fakevideo", file_name="ad_video.mp4", mime="video/mp4")

st.markdown("---")
st.caption("Frontend pasand aaya? Bata – ab backend + real video generation (images, audio, moviepy) add karein? Ya kuch change chahiye design mein?")
