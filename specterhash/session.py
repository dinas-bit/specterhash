"""Session logging and history."""
import json
import time
import logging
from pathlib import Path

logger = logging.getLogger("specterhash.session")

class SessionLogger:
    def __init__(self, log_dir: str = "sessions/"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.entries = []
    def log(self, action: str, details: dict):
        entry = {"timestamp": time.time(), "action": action, "details": details}
        self.entries.append(entry)
    def save(self):
        path = self.log_dir / f"session_{int(time.time())}.json"
        with open(path, "w") as f:
            json.dump(self.entries, f, indent=2)
        logger.info(f"Session saved: {path}")
