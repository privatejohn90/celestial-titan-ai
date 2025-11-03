# ==========================================================
# 🌌 Celestial Titan God AI v70.3 — Full Restoration Build
# Cosmic Blue Edition ✨
# ==========================================================

import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import os, json, datetime, random
from datetime import date

# ====== TITAN CORE MODULES ======
from titan_core.quad_analyzer import analyze_quads
from titan_core.triple_detector import detect_triples
from titan_core.titan_db import init_db, save_draw, check_hit_status
from titan_core.cosmic_engine import get_cosmic_energy
from titan_core.fetch_results import fetch_latest_result
from titan_core.memory_engine import log_result, get_recent_results

# ====== SIDEBAR HEADER ======
st.sidebar.markdown("### 💫 Celestial Titan God AI v70.3")
st.sidebar.caption("Core modules: Chat, Quad, Triple, DB, Cosmic Engine")

# ==========================================================
# ⚙️ AUTO-FETCH & MEMORY — Titan v70.3
# ==========================================================
st.sidebar.markdown("### ⚙️ Auto-Fetch & Memory")

if st.sidebar.button("Fetch Latest Draw"):
    result = fetch_latest_result("fl_pick5")  # Example: Florida Pick5
    if "error" not in result:
        log_result(result)
        st.sidebar.success(f"Fetched {result['state']} → {result['numbers']}")
    else:
        st.sidebar.error(result["error"])

recent = get_recent_results()
if recent:
    last = recent[0]
    st.sidebar.info(f"🧠 Last fetched: {last.get('state','?')} — {last.get('numbers','?')}")

# ==========================================================
# 🌈 PAGE CONFIGURATION
# ==========================================================
st.set_page_config(page_title="Celestial Titan God AI", page_icon="💎", layout="wide")

# ==========================================================
# 🌌 COSMIC BLUE THEME
# ==========================================================
st.markdown("""
<style>
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#041024 0%,#081C3A 100%);
  color: #E0E0E0;
}
[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 20% 20%,#091530 0%,#0C1020 35%,#05080F 100%);
}
h1,h2,h3,h4,h5,h6,p,div {color:#E0E0E0!important;}
hr {border:0.5px solid #2A2A4A;}
.stButton>button {
  background:linear-gradient(90deg,#0040FF,#0088FF);
  color:white;
  border:none;
  border-radius:8px;
  padding:0.4em 1.2em;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 🌠 MAIN DISPLAY
# ==========================================================
st.title("💎 Celestial Titan God AI v70.3 — Cosmic Blue Edition")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔢 Quad & Triple Analyzer")
    sample_draw = st.text_input("Enter draw result:", "70089")
    if st.button("Analyze Pattern"):
        quad_info = analyze_quads(sample_draw)
        triple_info = detect_triples(sample_draw)
        st.markdown("### Quad Analysis Result")
        st.info(quad_info)
        st.markdown("### Triple Detection Result")
        st.info(triple_info)

with col2:
    st.subheader("🌙 Cosmic Energy")
    energy = get_cosmic_energy()
    st.metric("Titan Energy Reading", f"{energy}%")
    if energy >= 80:
        st.success("🟢 Stable cosmic surge — Titan is aligned.")
    elif energy >= 50:
        st.warning("🟡 Medium fluctuation — active phase.")
    else:
        st.error("🔴 High distortion — grid instability detected.")

st.markdown("---")
st.caption("Powered by Celestial Titan God AI Engine — v70.3")
