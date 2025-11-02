# ==========================================================
# 🌙 Cosmic Engine — Celestial Titan God AI v70.3
# ==========================================================
import random, datetime

def get_cosmic_energy() -> dict:
    """
    Generates pseudo-cosmic data used for Titan's visual pulse.
    Combines lunar phase, temporal energy, and stability metrics.
    """

    phases = [
        ("New Moon", 10),
        ("First Quarter", 25),
        ("Full Moon", 100),
        ("Waning Gibbous", 65),
        ("Last Quarter", 35),
        ("Waning Crescent", 15),
        ("Waxing Crescent", 20),
        ("Waxing Gibbous", 80),
    ]
    phase, energy = random.choice(phases)
    pulse = random.choice(["Stable", "Active Load", "High Surge"])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simulate a stable cosmic summary for display in the sidebar
    summary = f"🪐 Phase: {phase} — Cosmic Energy {energy}% — {pulse} mode."

    return {
        "phase": phase,
        "energy": energy,
        "pulse": pulse,
        "summary": summary,
        "timestamp": timestamp
    }
