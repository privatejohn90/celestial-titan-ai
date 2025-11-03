# ==========================================================
# 🧠 Memory Engine — Celestial Titan God AI v70.4
# ==========================================================
import json, os, datetime

MEMORY_FILE = "titan_memory.json"

def log_result(entry: dict):
    """Saves fetched results into Titan’s long-term memory (JSON)."""
    data = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    entry["timestamp"] = str(datetime.datetime.now())
    data.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_recent_results(limit=5):
    """Returns the most recent X results from Titan’s memory."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            return data[-limit:]
    except:
        return []
