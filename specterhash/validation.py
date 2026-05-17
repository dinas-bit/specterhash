"""Configuration and input validation."""
import os
from typing import List, Optional

class Validator:
    @staticmethod
    def validate_hash(hash_str: str) -> bool:
        if not hash_str: return False
        valid_chars = set("0123456789abcdefABCDEF$_.")
        return all(c in valid_chars for c in hash_str)

    @staticmethod
    def validate_file(path: str) -> bool:
        return os.path.exists(path) and os.path.isfile(path)

    @staticmethod
    def validate_wordlist(path: str) -> List[str]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Wordlist not found: {path}")
        with open(path, errors="ignore") as f:
            return [l.strip() for l in f if l.strip()]
