"""Breach database management."""
import logging
import hashlib
from pathlib import Path
from typing import Set, Optional

logger = logging.getLogger("specterhash.breach")

class BreachDatabase:
    """Load and query password breach databases."""

    def __init__(self):
        self.passwords: Set[str] = set()
        self.hashes: Set[str] = set()

    def load_wordlist(self, path: str):
        with open(path, errors="ignore") as f:
            for line in f:
                pw = line.strip()
                if pw:
                    self.passwords.add(pw.lower())
        logger.info(f"Loaded {len(self.passwords)} passwords")

    def load_hashes(self, path: str):
        with open(path) as f:
            for line in f:
                h = line.strip().split(":")[-1].strip()
                if h:
                    self.hashes.add(h.lower())
        logger.info(f"Loaded {len(self.hashes)} hashes")

    def check_password(self, password: str) -> bool:
        return password.lower() in self.passwords

    def check_hash(self, hash_value: str) -> bool:
        return hash_value.lower() in self.hashes

    def count(self) -> int:
        return len(self.passwords)
