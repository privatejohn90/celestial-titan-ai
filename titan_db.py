# ==========================================================
# 💾 Titan Database Engine — Celestial Titan God AI v70.3
# ==========================================================
import sqlite3, os, datetime

DB_PATH = "titan_history.db"

def init_db():
    """Initialize database and create table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS draws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            state TEXT,
            game TEXT,
            draw_time TEXT,
            result TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_draw(date, state, game, draw_time, result, status="Analyzed"):
    """Save a draw result into Titan’s historical archive."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO draws (date, state, game, draw_time, result, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (date, state, game, draw_time, result, status))
    conn.commit()
    conn.close()

def check_hit_status(result):
    """
    Simple check — returns “FORECAST” if already saved as forecast pattern,
    else returns “ARCHIVED”.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM draws WHERE result=? AND status='FORECAST'", (result,))
    count = c.fetchone()[0]
    conn.close()
    return "FORECAST" if count > 0 else "ARCHIVED"

def list_recent_draws(limit=10):
    """Return recent draws for Titan memory dashboard."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT date, state, game, draw_time, result, status FROM draws ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows
