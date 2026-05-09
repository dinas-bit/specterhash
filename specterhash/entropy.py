"""Password entropy and strength analysis."""
import math
import logging
import string
from typing import Dict, List

logger = logging.getLogger("specterhash.entropy")

class EntropyAnalyzer:
    """Analyze password entropy and strength."""

    CHARSETS = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "special": string.punctuation,
    }

    def calculate_entropy(self, password: str) -> float:
        charset_size = 0
        if any(c in string.ascii_lowercase for c in password): charset_size += 26
        if any(c in string.ascii_uppercase for c in password): charset_size += 26
        if any(c in string.digits for c in password): charset_size += 10
        if any(c in string.punctuation for c in password): charset_size += 32
        if charset_size == 0: return 0
        return len(password) * math.log2(charset_size)

    def strength_label(self, entropy: float) -> str:
        if entropy < 28: return "Very Weak"
        if entropy < 36: return "Weak"
        if entropy < 60: return "Reasonable"
        if entropy < 128: return "Strong"
        return "Very Strong"

    def analyze(self, password: str) -> Dict:
        entropy = self.calculate_entropy(password)
        return {
            "password_length": len(password),
            "entropy_bits": round(entropy, 2),
            "strength": self.strength_label(entropy),
            "has_lower": any(c in string.ascii_lowercase for c in password),
            "has_upper": any(c in string.ascii_uppercase for c in password),
            "has_digit": any(c in string.digits for c in password),
            "has_special": any(c in string.punctuation for c in password),
        }

    def analyze_batch(self, passwords: List[str]) -> Dict:
        results = [self.analyze(pw) for pw in passwords]
        avg_entropy = sum(r["entropy_bits"] for r in results) / len(results)
        weak_count = sum(1 for r in results if r["entropy_bits"] < 36)
        return {"total": len(results), "avg_entropy": avg_entropy, "weak_count": weak_count, "results": results}
