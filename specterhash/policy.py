"""Password policy enforcement."""
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass

logger = logging.getLogger("specterhash.policy")

@dataclass
class PasswordPolicy:
    min_length: int = 8
    max_length: int = 128
    require_uppercase: bool = True
    require_lowercase: bool = True
    require_digit: bool = True
    require_special: bool = False
    max_consecutive: int = 3
    min_entropy: float = 28.0

class PolicyEngine:
    """Enforce password policies."""

    def __init__(self, policy: PasswordPolicy = None):
        self.policy = policy or PasswordPolicy()

    def check(self, password: str) -> Dict:
        violations = []
        if len(password) < self.policy.min_length:
            violations.append(f"Too short ({len(password)} < {self.policy.min_length})")
        if self.policy.require_uppercase and not any(c.isupper() for c in password):
            violations.append("No uppercase")
        if self.policy.require_lowercase and not any(c.islower() for c in password):
            violations.append("No lowercase")
        if self.policy.require_digit and not any(c.isdigit() for c in password):
            violations.append("No digit")
        for i in range(len(password) - self.policy.max_consecutive + 1):
            if len(set(password[i:i+self.policy.max_consecutive])) == 1:
                violations.append(f"Too many consecutive identical chars")
                break
        return {"password_length": len(password), "violations": violations, "pass": len(violations) == 0}
