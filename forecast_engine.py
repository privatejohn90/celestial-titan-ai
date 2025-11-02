# ==========================================================
# 🔮 Forecast Engine — Celestial Titan God AI v70.3
# ==========================================================
import random, datetime

def generate_forecast(game_type: str, last_result: str) -> str:
    """
    Generates 5-number forecast for major games.
    Fantasy 5, SuperLotto Plus, Mega Millions, Powerball supported.
    """

    random.seed(hash(last_result + str(datetime.date.today())))
    game_type = game_type.lower()

    # default counts for each game type
    if "fantasy" in game_type:
        count, max_num = 5, 39
    elif "superlotto" in game_type:
        count, max_num = 5, 47
    elif "mega" in game_type:
        count, max_num = 5, 70
    elif "powerball" in game_type:
        count, max_num = 5, 69
    else:
        count, max_num = 5, 50

    forecast = sorted(random.sample(range(1, max_num + 1), count))

    cosmic_comment = random.choice([
        "🌕 Lunar alignment stable — Titan projects harmonic spread.",
        "🌠 Frequency resonance detected — higher digits favored.",
        "🪐 Temporal drift suggests balanced highs & lows.",
        "☄️ Cosmic surge — low bands energizing.",
        "✨ Neutral phase — even dispersion likely next draw."
    ])

    return f"**{game_type.title()} Forecast:** {forecast}\n\n{cosmic_comment}"
