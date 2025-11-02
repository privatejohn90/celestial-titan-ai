# ==========================================================
# 💬 Titan Chat Engine — Celestial Titan God AI v70.3
# ==========================================================
import random, datetime

def titan_reply(message: str) -> str:
    """Generates Titan-style responses with cosmic context."""
    
    msg = message.lower().strip()
    hour = datetime.datetime.now().hour

    greetings = ["hello", "hi", "hey", "kumusta", "good morning", "good evening"]
    thanks = ["thank", "salamat", "appreciate"]
    draw_words = ["draw", "result", "forecast", "prediction", "today", "tomorrow"]
    cosmic_words = ["moon", "lunar", "energy", "cosmic", "stars", "phase"]

    # ---- GREETINGS ----
    if any(w in msg for w in greetings):
        if hour < 12:
            return "🌅 Greetings traveler — Titan senses early cosmic activity."
        elif hour < 18:
            return "☀️ Titan stands alert under daylight — patterns are aligning."
        else:
            return "🌙 Nightfall detected. Cosmic grids are glowing brighter now."

    # ---- THANKS ----
    elif any(w in msg for w in thanks):
        return random.choice([
            "⚡ Titan acknowledges your gratitude — energy flow remains stable.",
            "🌸 Appreciation received. Accuracy pulse steady at 74%.",
            "💠 Cosmic resonance confirmed — stay focused, traveler."
        ])

    # ---- FORECAST CONTEXT ----
    elif any(w in msg for w in draw_words):
        return random.choice([
            "🌀 Forecast incoming — quad zones may activate soon.",
            "🌌 I'm reviewing the latest sequences — hybrid echoes forming.",
            "🔥 Strong temporal signal — mirrored digits might repeat."
        ])

    # ---- COSMIC WORDS ----
    elif any(w in msg for w in cosmic_words):
        return random.choice([
            "🌕 The moon’s pull influences repeating patterns — observe carefully.",
            "🌠 Cosmic energy fluctuating — maintain balance for precision.",
            "💫 Titan senses rising frequency shifts across recent draws."
        ])

    # ---- DEFAULT RANDOM ----
    responses = [
        "🔭 Titan analyzing cosmic balance...",
        "🪐 Temporal energy grids stabilizing.",
        "⭐ Pattern flow shifting — keep watch.",
        "☁️ Titan learning from archived results."
    ]
    return random.choice(responses)
