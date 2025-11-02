# ==========================================================
# 🔁 Triple Detector — Celestial Titan God AI v70.3
# ==========================================================
import random

def detect_triples(result: str) -> str:
    """
    Detects triple patterns and mirrored sequences.
    Returns Titan’s interpretive message.
    """

    result = result.strip()
    if not result.isdigit():
        return "⚠️ Invalid input — digits only."

    digits = list(result)
    counts = {d: digits.count(d) for d in set(digits)}

    triples = [d for d, c in counts.items() if c == 3]
    mirrors = []

    # Detect mirror pattern (like 1221, 3443, etc.)
    if result == result[::-1]:
        mirrors.append(result)

    output = []

    if triples:
        d = triples[0]
        output.append(f"⚡ **Triple detected:** {d*3}")
        output.append("🪞 Repeating trinity — Titan senses rotational symmetry forming.")
    elif mirrors:
        output.append(f"🌗 **Mirror pattern detected:** {mirrors[0]}")
        output.append("🌠 Energy reflection noted — probability of echo hits increases.")
    else:
        output.append("🌌 No triple or mirror structures found — dispersion stable.")
        output.append("🧭 Titan advises patience; echo cycle may restart soon.")

    flavor = [
        "💫 Quantum drift aligning with mirrored resonance.",
        "🧩 Low-frequency vibration steady — next cycle may show duplication.",
        "🌕 Temporal loop flattening — energy neutralized for now.",
        "🔥 Cosmic tri-pulse weakening — calm before surge."
    ]
    output.append(random.choice(flavor))

    return "\n".join(output)
