# ==========================================================
# 💾 Titan Database Engine — Celestial Titan God AI v70.3
# ==========================================================
import sqlite3, json, os
from datetime import datetime

DB_PATH = "titan_history.db"

# --- Initialize Database ---
def init_db():
    """Creates the database and draws table if not existing."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS draws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game TEXT,
            date TEXT,
            result TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

# --- Save a Draw Result ---
def save_draw(game: str, result: str, status: str = "FORECAST"):
    """Saves a draw into the Titan database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO draws (game, date, result, status) VALUES (?,?,?,?)",
        (game, datetime.now().strftime("%Y-%m-%d %H:%M"), result, status)
    )
    conn.commit()
    conn.close()

# --- Retrieve Draw History ---
def get_draws(limit: int = 10):
    """Fetches recent draws from the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT game, date, result, status FROM draws ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()

    data = []
    for r in rows:
        data.append({
            "game": r[0],
            "date": r[1],
            "result": r[2],
            "status": r[3]
        })
    return data
