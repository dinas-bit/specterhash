"""Dictionary-based password checking."""
import logging
from typing import List, Set

logger = logging.getLogger("specterhash.dictionary")

class DictionaryChecker:
    def __init__(self):
        self.dictionaries: Set[str] = set()
    def load(self, path: str):
        with open(path, errors="ignore") as f:
            self.dictionaries.update(l.strip().lower() for l in f if l.strip())
        logger.info(f"Loaded {len(self.dictionaries)} entries")
    def check(self, password: str) -> bool:
        return password.lower() in self.dictionaries
    def check_batch(self, passwords: List[str]) -> List[dict]:
        return [{"password": p, "in_dictionary": self.check(p)} for p in passwords]
