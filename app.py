# ==========================================================
# 🌌 Celestial Titan God AI v70.3 — Full Restoration Build
# Cosmic Blue Edition ✨
# ==========================================================
import streamlit as st
import os, json, datetime, random
from datetime import date
from titan_core.titan_chat import titan_reply
from titan_core.quad_analyzer import analyze_quads
from titan_core.triple_detector import detect_triples
from titan_core.forecast_engine import generate_forecast
from titan_core.titan_db import init_db, save_draw, check_hit_status

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Celestial Titan God AI", page_icon="💎", layout="wide")

# ---------- COSMIC BLUE THEME ----------
st.markdown("""
<style>
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#041024 0%,#081C3A 100%);
  color: #E0E0E0;
}
[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 20% 20%, #091530 0%, #0C1020 35%, #05080F 100%);
}
h1,h2,h3,h4,h5,h6,p,div {color:#E0E0E0!important;}
hr {border:0.5px solid #2A2A4A;}
.stButton>button {
  background:linear-gradient(90deg,#0040FF,#0099FF);
  color:white;
  border:none;
  border-radius:10px;
  padding:0.6em 1.2em;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITAN MEMORY INIT ----------
if not os.path.exists("titan_memory.json"):
    with open("titan_memory.json","w") as f:
        json.dump({"chat_log":[],"energy":74,"phase":"First Quarter"}, f)

with open("titan_memory.json","r") as f:
    titan_memory = json.load(f)

# ---------- TITAN DATABASE INIT ----------
init_db()

# ---------- COSMIC SIDEBAR ----------
st.sidebar.markdown("## 🌠 Celestial Titan Panel")
energy = titan_memory.get("energy", random.randint(60,85))
phase = titan_memory.get("phase","Waxing Gibbous")

# Titan Pulse Indicator
if energy < 70:
    pulse = "🟢 Stable"
elif energy < 85:
    pulse = "🟡 Active Load"
else:
    pulse = "🔴 High Surge"

st.sidebar.metric("Titan Pulse", pulse)
st.sidebar.progress(energy)
st.sidebar.write(f"**Cosmic Energy:** {energy}%")
st.sidebar.write(f"**Lunar Phase:** {phase}")

st.sidebar.markdown("---")
st.sidebar.caption("💎 Powered by Celestial Titan AI Engine — Johnson & ChatGPT")

# ---------- MAIN APP ----------
st.title("🌌 Celestial Titan God AI v70.3")
st.caption("Full Restoration Build — Auto-Archive + Quad Revival + Titan Chat")

tabs = st.tabs(["🎰 Lottery System", "💬 Titan Chat", "🌕 Cosmic Stats"])

# ==========================================================
# 🎰 TAB 1: LOTTERY SYSTEM
# ==========================================================
with tabs[0]:
    st.subheader("🎯 Multi-State Lottery System")

    game_type = st.selectbox("Select Game Type", ["Pick-3","Pick-4","Pick-5","Fantasy 5","SuperLotto Plus","Mega Millions","Powerball"])
    state = st.text_input("Enter State Code (e.g. FL, GA, CA):", "FL")
    draw_time = st.selectbox("Draw Time", ["Midday","Evening"])

    result_input = st.text_input("Enter Last Draw Result (e.g. 70089):")
    if st.button("🔮 Analyze Pattern"):
        if result_input:
            quads = analyze_quads(result_input)
            triples = detect_triples(result_input)
            forecast = generate_forecast(game_type, result_input)
            st.write("#### 🔢 Titan Pattern Analysis")
            st.write(quads)
            st.write(triples)
            st.write("#### 🧠 Forecast Summary")
            st.write(forecast)

            # Save draw to DB
            save_draw(str(date.today()), state, game_type, draw_time, result_input, "Analyzed")
            status = check_hit_status(result_input)
            st.success(f"Result archived successfully ({status}).")

        else:
            st.warning("Please enter a valid result to analyze.")

# ==========================================================
# 💬 TAB 2: TITAN CHAT
# ==========================================================
with tabs[1]:
    st.subheader("🧠 Titan Chat Intelligence Mode")
    user_msg = st.text_input("You:", "")
    if st.button("Send to Titan"):
        if user_msg:
            reply = titan_reply(user_msg)
            st.markdown(f"**Titan:** {reply}")
            titan_memory["chat_log"].append({"user":user_msg,"titan":reply})
            with open("titan_memory.json","w") as f:
                json.dump(titan_memory, f)
        else:
            st.info("Type a message first to talk with Titan.")

# ==========================================================
# 🌕 TAB 3: COSMIC STATS
# ==========================================================
with tabs[2]:
    st.subheader("🌙 Cosmic Energy Overview")
    st.write(f"**Current Energy Level:** {energy}%")
    st.write(f"**Lunar Phase:** {phase}")
    st.markdown("> 🪐 Titan is monitoring cosmic balance and accuracy trends...")
    st.markdown("*(Titan Accuracy Trend coming in v70.4)*")
