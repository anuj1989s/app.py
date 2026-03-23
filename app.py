import streamlit as st
import time

st.set_page_config(
    page_title="Anuj AI Ad Forge - Instant AI Product Ads",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Full cyberpunk/neon landing CSS (inspired by AdsGPT + futuristic trends)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;600;800&display=swap');

    .stApp {
        background: #000 url('https://images.unsplash.com/photo-1557683316-973673baf926?auto=format&fit=crop&q=80') no-repeat center center fixed;
        background-size: cover;
        color: #e0e0ff;
        font-family: 'Inter', sans-serif;
    }

    /* Hero with glow & stats */
    .hero {
        text-align: center;
        padding: 120px 20px 80px;
        background: linear-gradient(to bottom, rgba(10,0,30,0.85), rgba(0,0,0,0.95));
    }

    .hero h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        color: #ff00ff;
        text-shadow: 0 0 40px #ff00ff, 0 0 80px #00ffff;
        margin: 0;
        animation: neon-pulse 4s infinite alternate;
    }

    @keyframes neon-pulse {
        0% { text-shadow: 0 0 20px #ff00ff; opacity: 0.9; }
        100% { text-shadow: 0 0 60px #ff00ff, 0 0 100px #00ffff; opacity: 1; }
    }

    .stats {
        display: flex;
        justify-content: center;
        gap: 60px;
        flex-wrap: wrap;
        margin: 40px 0;
        font-size: 1.4rem;
        color: #00ffff;
    }

    .stat {
        text-align: center;
        padding: 20px;
        background: rgba(0,255,255,0.05);
        border: 1px solid #00ffff44;
        border-radius: 12px;
        min-width: 180px;
    }

    .tagline {
        font-size: 1.8rem;
        color: #00ffff;
        max-width: 900px;
        margin: 30px auto;
    }

    /* Features grid */
    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 30px;
        padding: 60px 20px;
        max-width: 1200px;
        margin: 0 auto;
    }

    .feature {
        background: rgba(20,0,50,0.7);
        border: 1px solid #ff00ff33;
        border-radius: 16px;
        padding: 40px 30px;
        text-align: center;
        transition: all 0.4s;
    }

    .feature:hover {
        transform: translateY(-15px);
        box-shadow: 0 20px 60px rgba(255,0,255,0.3);
        border-color: #ff00ff;
    }

    .feature h3 {
        color: #ff00ff;
        font-size: 1.6rem;
        margin-bottom: 15px;
    }

    /* Input & CTA */
    .input-cta {
        max-width: 1000px;
        margin: 0 auto 80px;
        padding: 0 20px;
    }

    .stTextArea textarea {
        background: rgba(10,5,30,0.85) !important;
        border: 2px solid #00ffff !important;
        color: #fff !important;
        border-radius: 20px !important;
        font-size: 1.2rem !important;
        min-height: 180px !important;
        box-shadow: 0 0 30px rgba(0,255,255,0.3) !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #ff00ff, #00ffff) !important;
        color: #000 !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        padding: 20px 80px !important;
        border-radius: 50px !important;
        box-shadow: 0 0 40px #ff00ff80 !important;
        border: none !important;
        transition: all 0.4s;
        display: block !important;
        margin: 40px auto 0 !important;
    }

    .stButton > button:hover {
        box-shadow: 0 0 80px #00ffff !important;
        transform: scale(1.08);
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
    <div class="hero">
        <h1>ANUJ AI AD FORGE</h1>
        <p class="tagline">Prompt Daalo – AI Seconds Mein High-Converting Product Video Ad Bana De<br>Scene-by-Scene Breakdown • Auto Hindi/English Audio • Neon Visuals & CTA</p>
        
        <div class="stats">
            <div class="stat"><strong>1M+</strong><br>Ads Generated</div>
            <div class="stat"><strong>100K+</strong><br>Happy Creators</div>
            <div class="stat"><strong>500+</strong><br>Platforms Optimized</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Features
st.markdown("""
    <div class="features">
        <div class="feature">
            <h3>⚡ Instant AI Magic</h3>
            <p>15-90 sec professional ads – no editing skills needed</p>
        </div>
        <div class="feature">
            <h3>🎤 Natural Voice Narration</h3>
            <p>Hindi/English auto audio + background music sync</p>
        </div>
        <div class="feature">
            <h3>🔥 Scene Breakdown Power</h3>
            <p>Auto visuals, transitions, text overlays, price tags</p>
        </div>
        <div class="feature">
            <h3>📈 Competitor-Inspired</h3>
            <p>Best practices se high-conversion ads</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Input Section
st.markdown('<div class="input-cta">', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1.3])

with col1:
    prompt = st.text_area(
        "**Apna Product Ad Prompt Daalo (Detail jitna zyada, result utna killer)**",
        placeholder="उदाहरण: प्रीमियम वायरलेस ईयरबड्स का 45 सेकंड साइबरपंक ऐड – रेनी नाइट सिटी, रनर glowing implants के साथ, bass drop highlight, sweat-proof, 40hr battery, ₹1999 में, end में glitchy 'Order Now' hologram CTA!",
        height=180
    )

with col2:
    duration = st.slider("Ad Duration (seconds)", 15, 90, 30)
    lang = st.selectbox("Voice Language", ["Hindi (hi)", "English (en)"], index=0)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 GENERATE YOUR NEON AD NOW 🚀"):
    if not prompt:
        st.error("Prompt daal bhai, warna AI wait karega! 😈")
    else:
        with st.spinner("Neon circuits firing... scenes rendering... audio synth on..."):
            time.sleep(4)  # real mein yahan LLM + gen APIs
            st.success("Ad Forged in Neon! Download kar le 🔥")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # placeholder
            st.download_button("⬇️ Download Ad Video", "demo.mp4", "anuj_ad.mp4")

st.markdown("""
    <div style="text-align:center; color:#888; padding:60px 0; font-size:1.1rem;">
        Powered by Grok AI • Built in Bhopal • Join the future of product ads
    </div>
""", unsafe_allow_html=True)
