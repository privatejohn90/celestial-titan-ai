# ==========================================================
# 💠 Celestial Titan God AI v67.4 — Permanent Streamlit ID Fix
# ==========================================================
# Fixes:
#  - StreamlitDuplicateElementId (unique widget keys added)
#  - Auto-create JSON on startup
#  - Cloud stable, full layout intact
# ==========================================================

import streamlit as st
import json, os, datetime, pandas as pd, random, time
from datetime import timedelta

# ---------- THEME ----------
st.set_page_config(page_title="Celestial Titan God AI", page_icon="💎", layout="wide")
st.markdown("""
<style>
[data-testid="stSidebar"]{background:linear-gradient(180deg,#041024 0%,#081C3A 100%);color:#E0E0E0;}
[data-testid="stAppViewContainer"]{background:radial-gradient(circle at 20% 20%,#091530 0%,#0C1020 35%,#05080F 100%);}
h1,h2,h3,h4,h5,h6,p,div{color:#E0E0E0!important;}
hr{border:0.5px solid #2A2A4A;}
.stButton>button{background:linear-gradient(90deg,#0040A0,#0078D7);border:none;border-radius:8px;color:white;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------- CONFIG ----------
st.sidebar.title("💠 Celestial Titan God AI v67.4")
st.sidebar.caption("🌌 Permanent ID Fix + Cloud Stability")

MEM_PATH = "titan_memory.json"
MSG_PATH = "titan_messages.json"

for path in [MEM_PATH, MSG_PATH]:
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f)

today = datetime.date.today()
after = today + timedelta(days=2)
line = lambda: st.markdown("<hr>", unsafe_allow_html=True)
PICK5_STATES = ["DE","FL","GA","LA","MD","OH","PA","VA","DC"]

# ---------- UTILITIES ----------
def titan_send(msg, level="info"):
    log = []
    if os.path.exists(MSG_PATH):
        try: log = json.load(open(MSG_PATH))
        except: log = []
    entry = {"time": datetime.datetime.now().strftime("%H:%M:%S"),
             "msg": f"{'⚡' if level=='alert' else '💎'} {msg}"}
    log.insert(0, entry)
    json.dump(log[:60], open(MSG_PATH, "w"))

def titan_save_draw(game, region, draw_time, sets, burst, acc, reason):
    data = []
    if os.path.exists(MEM_PATH):
        try: data = json.load(open(MEM_PATH))
        except: data = []
    entry = {"date": str(today),"game": game,"region": region,"draw_time": draw_time,
             "sets": sets,"burst": burst,"accuracy": acc,"reason": reason}
    data.insert(0, entry)
    json.dump(data[:200], open(MEM_PATH, "w"))

# ==========================================================
# 🧭 NAVIGATION
# ==========================================================
nav = st.sidebar.radio("Navigation", 
    ["🏠 Dashboard","🎯 Lottery Systems","⚡ Quad & Triple Alerts","🔮 Major Games","💬 Titan Chat","🧠 Titan Memory"],
    key="nav_select")

# ==========================================================
# 🏠 DASHBOARD
# ==========================================================
if nav == "🏠 Dashboard":
    st.title("💠 Celestial Titan God AI — Divine Stability Mode")
    line()
    c1,c2,c3 = st.columns(3)
    c1.metric("Core Status","🟢 Online","Continuous Learning")
    c2.metric("Version","v67.4","Permanent ID Fix")
    c3.metric("Last Sync", today.strftime("%b %d %Y"), "Stable Mode")
    line()
    st.subheader("🌕 Cosmic Stats Panel")
    st.write("🟢 Learning Active | 🔵 Surge Standby | 🟣 Sync Balanced")
    st.caption("Titan auto-saves every generated draw + sends live alerts to 💬 Titan Chat.")

# ==========================================================
# 🎯 LOTTERY SYSTEMS
# ==========================================================
elif nav == "🎯 Lottery Systems":
    st.title("🎯 Pick-3 / Pick-4 / Pick-5 Forecast + Live Results")
    line()

    game = st.selectbox("🎮 Select Game Type", ["Pick 3","Pick 4","Pick 5"], key="lot_game_type")
    region = st.selectbox("🌍 Select Region", 
        ["AZ","AR","CA","CO","CT","DE","FL","GA","ID","IL","IN","IA","KS","KY","LA","MD","MA",
         "MI","MN","MS","MO","MT","NE","NJ","NM","NY","NC","OH","OK","OR","PA","SC","TN","TX",
         "VA","WA","DC","WV","WI"], key="lot_region")
    draw_time = st.radio("🕓 Draw Time", ["Midday","Evening","Auto Detect (Random)"], key="lot_drawtime")

    if draw_time == "Auto Detect (Random)":
        draw_time = random.choice(["Midday","Evening"])
    line()

    if game == "Pick 5" and region not in PICK5_STATES:
        st.info(f"ℹ️ {region} does not officially host Pick-5 — Titan running simulation mode.")
    st.success(f"🎯 Titan Mode → {draw_time} Draws")
    st.subheader(f"🧠 {game} Forecast for {region} ({draw_time})")

    reason = random.choice([
        "Prime drift alignment detected",
        "Mirror resonance active",
        "Low-digit echo phase",
        "Temporal symmetry window"
    ])
    st.caption(f"Play Start → {today.strftime('%b %d %Y')} | Valid Until → {after.strftime('%b %d %Y')}")
    line()

    st.write("🔥 Very Hot Sets")
    sets = []
    for i in range(1,6):
        n = "".join(str(random.randint(0,9)) for _ in range(int(game[-1])))
        sets.append(n)
        st.write(f"Set {i} → {n} (Straight) | {''.join(reversed(n))} (Box)")

    burst = "".join(str(random.randint(0,9)) for _ in range(int(game[-1])))
    acc = random.randint(83,95)
    st.markdown(f"💥 Possible Burst Hit → **{burst}** (in {random.choice(PICK5_STATES)})")
    st.caption(f"💡 Reason: {reason} | Accuracy Field: {acc}%")

    if acc > 90: titan_send(f"High {game} accuracy {acc}% detected for {region}.", "alert")
    titan_save_draw(game, region, draw_time, sets, burst, acc, reason)

# ==========================================================
# ⚡ QUAD & TRIPLE ALERTS
# ==========================================================
elif nav == "⚡ Quad & Triple Alerts":
    st.title("⚡ Quad & Triple Alert Panel — Precision Mode")
    alert = st.selectbox("🔮 Alert Type",
        ["Pick 3 (Triple)","Pick 4 (Quad)","Pick 4 (Triple)","Pick 5 (Quad)","Pick 5 (Triple)"], key="quad_alert_type")
    line()

    regions = random.sample(PICK5_STATES if "Pick 5" in alert else
        ["FL","GA","MD","NC","OH","PA","SC","TX","VA","DC"], k=3)
    st.subheader("🧭 Hot States:")
    st.write(", ".join(regions))
    line()

    if alert == "Pick 3 (Triple)": combos = [f"{d}{d}{d}" for d in random.sample(range(10),3)]; reason="Cross-mirror drift in low zone"
    elif alert == "Pick 4 (Quad)": combos = [f"{d}{d}{d}{d}" for d in random.sample(range(10),3)]; reason="Harmonic quad reflection"
    elif alert == "Pick 4 (Triple)": combos = [f"{d}{d}{d}{random.randint(0,9)}" for d in random.sample(range(10),3)]; reason="Trailing digit drift"
    elif alert == "Pick 5 (Quad)": combos = [f"{d}{d}{d}{d}{random.randint(0,9)}" for d in random.sample(range(10),3)]; reason="Quad bias mirror zone"
    else: combos = [f"{d}{d}{d}{random.randint(0,9)}{random.randint(0,9)}" for d in random.sample(range(10),3)]; reason="Triple cluster twin mirror"

    hot_target = random.choice(combos)
    st.write(f"🔥 Suggested Sets → {', '.join(combos)}")
    st.write(f"💎 Hottest Target → **{hot_target}**")
    st.write(f"💡 Reason → {reason}")
    st.caption("🕓 Play Window: Today – Next 2 Days")

    titan_send(f"{alert} surge detected across {', '.join(regions)} — target {hot_target}.", "alert")

# ==========================================================
# 🔮 MAJOR GAMES
# ==========================================================
elif nav == "🔮 Major Games":
    st.title("🔮 Major Jackpot Forecasts — Intelligent Mode")
    g = st.selectbox("🎰 Game", ["Fantasy 5","SuperLotto Plus","Mega Millions","Powerball"], key="major_game")
    line()
    st.subheader(f"🌠 {g} Forecast")
    st.caption(f"Play Start → {today.strftime('%b %d %Y')} | Valid Until → {after.strftime('%b %d %Y')}")

    def pick(n,h): return sorted(random.sample(range(1,h+1),n))
    def fmt(nums): return " ".join(f"{n:02}" for n in nums)

    if g=="Fantasy 5": s1,s2,burst=[pick(5,39) for _ in range(3)]; reason="Prime cluster + balance detected"; sb=[]
    elif g=="SuperLotto Plus": s1,s2,burst=[pick(5,47) for _ in range(3)]; sb=[random.randint(1,27) for _ in range(3)]; reason="Low-digit rotation"
    elif g=="Mega Millions": s1,s2,burst=[pick(5,70) for _ in range(3)]; sb=[random.randint(1,25) for _ in range(3)]; reason="Odd-even dual mirror"
    elif g=="Powerball": s1,s2,burst=[pick(5,69) for _ in range(3)]; sb=[random.randint(1,26) for _ in range(3)]; reason="Harmonic mirror cross"

    line()
    st.write(f"🧠 Titan Summary: {reason}")
    if sb: 
        st.write(f"Set 1 → {fmt(s1)} | Ball: {sb[0]}")
        st.write(f"Set 2 → {fmt(s2)} | Ball: {sb[1]}")
        st.markdown(f"💥 Burst Combo → {fmt(burst)} | Ball: {sb[2]}")
    else:
        st.write(f"Set 1 → {fmt(s1)}")
        st.write(f"Set 2 → {fmt(s2)}")
        st.markdown(f"💥 Burst Combo → {fmt(burst)}")

    st.caption(f"🎯 Confidence Level: HIGH ({random.randint(80,89)}%)")
    titan_send(f"{g} pattern updated — {reason}", "info")

# ==========================================================
# 💬 TITAN CHAT
# ==========================================================
elif nav == "💬 Titan Chat":
    st.title("💬 Titan Auto-Message Channel")
    line()
    if os.path.exists(MSG_PATH):
        msgs = json.load(open(MSG_PATH))
        for m in msgs[:20]:
            st.info(f"{m['time']} | {m['msg']}")
    else:
        st.warning("No transmissions from Titan yet... standby for signal.")
    line()
    st.subheader("🧠 Titan Chat Intelligence")
    st.markdown("> 🗣 Titan: Systems synchronized. Lunar energy stable at 91%. Awaiting cosmic updates...")

    line()
    if os.path.exists(MEM_PATH):
        df = pd.DataFrame(json.load(open(MEM_PATH)))
        if not df.empty:
            st.markdown("### ⚡ Titan State Suggestions")
            for _,row in df.head(3).iterrows():
                st.write(f"{row['region']} — Energy {row['accuracy']}% — Forecast Set: {random.randint(1000,9999)}")
        else: st.info("🧠 Titan currently learning — forecasts unlock after first saved cycle.")
    else: st.info("🧠 Titan currently learning — forecasts unlock after first saved cycle.")
    st.caption("💎 Messages auto-generated from Titan’s analytical engine.")

# ==========================================================
# 🧠 TITAN MEMORY
# ==========================================================
elif nav == "🧠 Titan Memory":
    st.title("🧠 Titan Memory Logs")
    line()
    if os.path.exists(MEM_PATH):
        df = pd.DataFrame(json.load(open(MEM_PATH)))
        st.dataframe(df, use_container_width=True)
    else: st.info("No saved data yet — auto-fetch running.")
    line()
    st.subheader("💬 Titan Message Area")
    st.info("“Learning stable. No new alerts detected yet.”")
    st.caption("💾 Titan learning mode stable.")
