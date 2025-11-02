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

    # --- Detect full quads (4 identical digits) ---
    quads = [d for d, c in counts.items() if c == 4]
    triples = [d for d, c in counts.items() if c == 3]
    pairs   = [d for d, c in counts.items() if c == 2]

    explanation = []

    if quads:
        d = quads[0]
        explanation.append(f"💥 **Quad detected:** {d*4} — extreme pattern convergence!")
        explanation.append("🌌 Titan notes this as a *rare energy spike* within the grid.")
    elif triples:
        d = triples[0]
        explanation.append(f"⚡ Near-Quad (Triple) detected: {d*3}")
        explanation.append("🧭 Potential hybrid echo zone forming — watch next draw cycle.")
    elif pairs:
        pair_text = ', '.join([p*2 for p in pairs])
        explanation.append(f"✨ Dual pairs found: {pair_text}")
        explanation.append("🔮 Balanced energy — moderate repeating influence.")
    else:
        explanation.append("🌠 No repeating digits — clean dispersion pattern.")
        explanation.append("🪐 Neutral phase. Titan senses calm before activity.")

    # --- Add random cosmic remark for flavor ---
    remarks = [
        "☄️ Cosmic tension rising around mirrored digits.",
        "🌙 Energy channels stabilizing after quad discharge.",
        "🌀 Temporal grid resetting — next 2 draws critical.",
        "⭐ Alignment steady — preparing for new resonance."
    ]
    explanation.append(random.choice(remarks))

    return "\n".join(explanation)
