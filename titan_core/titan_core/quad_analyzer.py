# ==========================================================
# 🔢 Quad Analyzer — Celestial Titan God AI v70.3
# ==========================================================
import random

def analyze_quads(result: str) -> str:
    """
    Detects quads and near-quads in a numeric draw result.
    Returns a formatted explanation string for Titan.
    """

    result = result.strip()
    if not result.isdigit():
        return "⚠️ Invalid input — digits only."

    digits = list(result)
    counts = {d: digits.count(d) for d in set(digits)}

    # --- Detect repeating structures ---
    quads = [d for d, c in counts.items() if c == 4]
    triples = [d for d, c in counts.items() if c == 3]
    pairs = [d for d, c in counts.items() if c == 2]

    explanation = []

    if quads:
        d = quads[0]
        explanation.append(f"💥 Quad detected: {d*4} — ultra-rare pattern convergence!")
        explanation.append("🌌 Titan marks this as a *high-energy anomaly* in the grid.")
    elif triples:
        d = triples[0]
        explanation.append(f"⚡ Near-Quad (Triple) detected: {d*3}")
        explanation.append("🧭 Hybrid echo zone forming — monitor upcoming draws.")
    elif len(pairs) >= 2:
        pair_text = ', '.join([p*2 for p in pairs])
        explanation.append(f"✨ Dual pairs detected: {pair_text}")
        explanation.append("🔮 Balanced repetition — mild repeating influence.")
    elif pairs:
        explanation.append(f"🔹 One repeating pair found: {pairs[0]*2}")
        explanation.append("🪐 Neutral phase — may evolve into a near-quad soon.")
    else:
        explanation.append("🌠 No repeating digits detected — stable dispersion pattern.")
        explanation.append("☁️ Titan senses a calm energy cycle.")

    remarks = [
        "☄️ Cosmic tension fluctuating near mirrored digits.",
        "🌙 Lunar resonance slightly elevating accuracy field.",
        "🌀 Temporal field resetting — next 2 draws are crucial.",
        "⭐ Stellar grid steady — low interference ahead."
    ]
    explanation.append(random.choice(remarks))

    return "\n".join(explanation)
