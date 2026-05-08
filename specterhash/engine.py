"""Core audit engine."""
import hashlib
import logging
import time
from typing import List, Dict, Optional
from .hash_types import HashType, detect_hash

logger = logging.getLogger("specterhash.engine")

class AuditEngine:
    """Password auditing and hash verification engine."""

    def __init__(self, device_id: int = 0):
        self.device_id = device_id
        self.stats = {"verified": 0, "weak": 0, "cracked": 0}

    def verify_hash(self, password: str, hash_value: str, hash_type: HashType = None) -> bool:
        if hash_type is None:
            hash_type = detect_hash(hash_value)
        if hash_type == HashType.MD5:
            return hashlib.md5(password.encode()).hexdigest() == hash_value
        if hash_type == HashType.SHA256:
            return hashlib.sha256(password.encode()).hexdigest() == hash_value
        return False

    def audit_batch(self, passwords: List[str], hashes: Dict[str, str]) -> Dict:
        start = time.perf_counter()
        results = {"weak": [], "strong": [], "cracked": []}
        for pw in passwords:
            for h, ht in hashes.items():
                if self.verify_hash(pw, h, ht):
                    results["cracked"].append({"hash": h, "password": pw})
        elapsed = time.perf_counter() - start
        results["elapsed"] = elapsed
        return results

    def get_stats(self) -> dict:
        return self.stats.copy()
