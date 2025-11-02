# ==========================================================
# 🔮 Triple Detector — Celestial Titan God AI v70.3
# ==========================================================
import random

def detect_triples(result: str) -> str:
    """
    Detects triple digits and twin structures in a draw.
    Returns an interpretation for Titan.
    """

    result = result.strip()
    if not result.isdigit():
        return "⚠️ Invalid input — digits only."

    digits = list(result)
    counts = {d: digits.count(d) for d in set(digits)}

    triples = [d for d, c in counts.items() if c == 3]
    pairs = [d for d, c in counts.items() if c == 2]

    explanation = []

    if triples:
        d = triples[0]
        explanation.append(f"🔥 Triple detected: {d*3}")
        explanation.append("🌌 Titan detects harmonic frequency — triple resonance zone active.")
    elif len(pairs) >= 2:
        pair_text = ', '.join([p*2 for p in pairs])
        explanation.append(f"✨ Dual pairs: {pair_text}")
        explanation.append("💫 Balanced twin energy detected — moderate resonance.")
    elif pairs:
        explanation.append(f"🔹 One pair found: {pairs[0]*2}")
        explanation.append("🪐 Mild temporal echo — low cosmic interference.")
    else:
        explanation.append("🌠 No triples or pairs — neutral state, clean temporal flow.")

    remarks = [
        "⭐ Energy grid stable — next draw may shift polarity.",
        "🌙 Slight lunar interference affecting odd digits.",
        "⚡ Resonance fading — Titan marking low probability field.",
        "🌞 Solar phase stabilizing repeating patterns."
    ]
    explanation.append(random.choice(remarks))

    return "\n".join(explanation)
