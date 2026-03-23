import streamlit as st
import time

st.set_page_config(page_title="Anuj AI Ad Forge", page_icon="⚡", layout="wide")

# Enhanced CSS for real landing page feel
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;600&display=swap');

    .stApp {
        background: #0d001a;
        color: #e0e0ff;
    }

    .hero {
        text-align: center;
        padding: 80px 20px 60px;
        background: linear-gradient(rgba(10,0,30,0.9), rgba(0,0,0,0.9));
        border-bottom: 1px solid #ff00ff33;
    }

    .hero h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        color: #ff00ff;
        text-shadow: 0 0 30px #ff00ff, 0 0 60px #00ffff;
        margin-bottom: 0.2rem;
        animation: glow 4s ease-in-out infinite alternate;
    }

    .hero p.tagline {
        font-size: 1.6rem;
        color: #00ffff;
        margin: 20px 0 40px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    @keyframes glow {
        from { text-shadow: 0 0 20px #ff00ff; }
        to   { text-shadow: 0 0 50px #ff00ff, 0 0 80px #00ffff; }
    }

    .features {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        padding: 60px 20px;
    }

    .feature-card {
        background: rgba(20,0,50,0.6);
        border: 1px solid #00ffff44;
        border-radius: 16px;
        padding: 30px;
        width: 320px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,255,255,0.15);
        transition: transform 0.3s, box-shadow 0.3s;
    }

    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(255,0,255,0.3);
    }

    .feature-card h3 {
        color: #ff00ff;
        margin-bottom: 15px;
    }

    .input-section {
        max-width: 900px;
        margin: 0 auto 60px;
        padding: 0 20px;
    }

    .stTextArea textarea {
        background: rgba(10,5,30,0.8) !important;
        border: 2px solid #00ffff !important;
        color: #e0e0ff !important;
        border-radius: 16px !important;
        font-size: 1.1rem !important;
        min-height: 160px !important;
        box-shadow: 0 0 25px rgba(0,255,255,0.2) !important;
    }

    .stButton button {
        background: linear-gradient(90deg, #ff00ff, #00ffff) !important;
        color: black !important;
        font-weight: bold !important;
        font-size: 1.4rem !important;
        padding: 18px 60px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 0 30px #ff00ff80 !important;
        transition: all 0.4s;
        width: 100% !important;
        max-width: 400px !important;
        margin: 30px auto 0 !important;
        display: block !important;
    }

    .stButton button:hover {
        box-shadow: 0 0 60px #00ffff !important;
        transform: scale(1.05);
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h1>ANUJ AI AD FORGE</h1>
        <p class="tagline">Prompt Daalo – AI Seconds Mein Scene-by-Scene Professional Product Ad Video Bana De<br>Auto Audio, Transitions, Call-to-Action Sab Included</p>
    </div>
""", unsafe_allow_html=True)

# Features
st.markdown("""
    <div class="features">
        <div class="feature-card">
            <h3>⚡ Instant Generation</h3>
            <p>15–90 second ads ready in moments – no editing needed</p>
        </div>
        <div class="feature-card">
            <h3>🎙️ Hindi/English Voice</h3>
            <p>Natural sounding narration + background music sync</p>
        </div>
        <div class="feature-card">
            <h3>🔥 Scene-by-Scene Magic</h3>
            <p>Auto breakdown + visuals + text overlays for max impact</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Main Input Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1.2])

with col1:
    prompt = st.text_area(
        "**Apna Product Ad Idea Daalo** (jitna detail utna behtar result)",
        placeholder="उदाहरण: एक प्रीमियम ब्लैक वायरलेस ईयरबड्स का 45 सेकंड का एनर्जेटिक प्रोडक्ट ऐड। युवा एथलीट जंगल में रनिंग कर रहा है, साउंड क्वालिटी हाइलाइट, स्वेट-प्रूफ, बैटरी 40 घंटे, सिर्फ ₹1999 में। आखिर में 'अभी ऑर्डर करो' CTA के साथ।",
        height=160
    )

with col2:
    duration = st.slider("वीडियो लंबाई", 15, 90, 30, step=5)
    lang = st.selectbox("Voice Language", ["Hindi", "English"], index=0)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 GENERATE AD NOW 🚀"):
    if not prompt.strip():
        st.error("Bhai prompt toh daal do pehle! 🔥")
    else:
        with st.spinner("AI circuits charging... scene breakdown + visuals + audio rendering..."):
            time.sleep(3.5)  # placeholder delay
            st.success("Ad taiyar! (Abhi demo mode – real video generation agle step mein)")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # real mein replace
            st.download_button("⬇️ Download Your Ad", "placeholder.mp4", "your_ad.mp4")

st.markdown("""
    <div style="text-align:center; color:#888; margin:60px 0;">
        <p>Powered by Grok AI • Made for creators in Bhopal • 1000+ ads generated vibe coming soon</p>
    </div>
""", unsafe_allow_html=True)
