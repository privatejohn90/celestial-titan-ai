# ==========================================================
# 🌌 Celestial Titan AI Pro v2.1 — Stability Pulse Build
# ==========================================================
import streamlit as st
import pandas as pd
from io import StringIO

# ---------- THEME ----------
st.set_page_config(page_title="Celestial Titan AI Pro", page_icon="💎", layout="wide")
st.markdown("""
<style>
[data-testid="stSidebar"] {
  background: linear-gradient(180deg,#041024 0%,#081C3A 100%);
  color: #E0E0E0;
}
[data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 25% 25%, #060D20 0%, #040817 40%, #00010A 100%);
}
h1,h2,h3,h4,h5,h6,p,div {color:#E0E0E0!important;}
hr {border:0.5px solid #2A2A4A;}
.stButton>button {
  background:linear-gradient(90deg,#0040FF,#0099FF);
  color:white;
  border-radius:5px;
  border:none;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🎯 Celestial Titan AI Pro v2 — Quad Sniper Analyzer")
st.caption("Analyze Pick-3/4/5 results, generate candidate sets, and track cosmic forecast energy.")

# ==========================================================
# 🔧 FIXED INPUT HANDLER — Prevent Duplicate Element IDs
# ==========================================================
def load_dataset(uploaded_file, game_type="Pick3"):
    """Loads dataset from file upload or pasted text."""
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df

    # Each game type gets its own text_area key (fixes DuplicateElementId)
    if game_type == "Pick3":
        sample_text = st.text_area("Paste CSV text (Pick 3 optional)", height=120, key="p3_text")
    elif game_type == "Pick4":
        sample_text = st.text_area("Paste CSV text (Pick 4 optional)", height=120, key="p4_text")
    elif game_type == "Pick5":
        sample_text = st.text_area("Paste CSV text (Pick 5 optional)", height=120, key="p5_text")
    else:
        sample_text = st.text_area("Paste CSV text (optional)", height=120, key="default_text")

    if not sample_text:
        st.info("No file or text uploaded. Using sample dataset.")
        df = pd.DataFrame({
            "date": ["2025-10-29", "2025-10-30", "2025-10-31"],
            "draw_time": ["Midday", "Evening", "Evening"],
            "numbers": ["134", "255", "409"]
        })
    else:
        try:
            df = pd.read_csv(StringIO(sample_text))
        except Exception:
            st.error("⚠️ Invalid CSV format. Please check your input.")
            return None

    return df

# ==========================================================
# 🔭 ANALYSIS CORE
# ==========================================================
def analyze_numbers(df, game_type):
    st.subheader(f"🔹 {game_type} Analysis Result")
    try:
        df['length'] = df['numbers'].astype(str).apply(len)
        avg_len = df['length'].mean()
        st.success(f"Dataset loaded successfully! Avg digit length: {avg_len:.2f}")
        st.dataframe(df)
        st.write("Titan Scan: Energy field stable 🔵")
    except Exception as e:
        st.error(f"⚠️ Error analyzing numbers: {e}")

# ==========================================================
# 🧩 MAIN INTERFACE
# ==========================================================
tab1, tab2, tab3 = st.tabs(["Pick 3", "Pick 4", "Pick 5"])

with tab1:
    st.subheader("🎲 Pick 3 Analyzer")
    uploaded = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"], key="p3_upload")
    df3 = load_dataset(uploaded, "Pick3")
    if st.button("Run Analysis (Pick 3)", key="run_p3"):
        if df3 is not None:
            analyze_numbers(df3, "Pick 3")

with tab2:
    st.subheader("🎲 Pick 4 Analyzer")
    uploaded = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"], key="p4_upload")
    df4 = load_dataset(uploaded, "Pick4")
    if st.button("Run Analysis (Pick 4)", key="run_p4"):
        if df4 is not None:
            analyze_numbers(df4, "Pick 4")

with tab3:
    st.subheader("🎲 Pick 5 Analyzer")
    uploaded = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"], key="p5_upload")
    df5 = load_dataset(uploaded, "Pick5")
    if st.button("Run Analysis (Pick 5)", key="run_p5"):
        if df5 is not None:
            analyze_numbers(df5, "Pick 5")

# ==========================================================
# 🪐 FOOTER
# ==========================================================
st.markdown("---")
st.markdown("""
<center>
🌙 **Powered by Celestial Titan AI Engine — Created by Johnson & ChatGPT**  
🟢 Stable Build v2.1 | 💠 Duplicate ID Fixed | 🔭 Ready for Titan Memory Integration
</center>
""", unsafe_allow_html=True)
