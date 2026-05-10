"""NIST SP 800-63B password compliance checking."""
import logging
from typing import Dict, List

logger = logging.getLogger("specterhash.compliance")

class ComplianceChecker:
    """Check passwords against NIST SP 800-63B guidelines."""

    BREACH_DATABASES = ["rockyou", "haveibeenpwned", "SecLists"]

    def __init__(self):
        self.breach_passwords = set()

    def load_breach_list(self, path: str):
        with open(path, errors="ignore") as f:
            self.breach_passwords = set(line.strip() for line in f)
        logger.info(f"Loaded {len(self.breach_passwords)} breach passwords")

    def check_nist(self, password: str) -> Dict:
        issues = []
        if len(password) < 8:
            issues.append("Too short (minimum 8 characters)")
        if password.lower() in self.breach_passwords:
            issues.append("Found in breach database")
        if password.lower() == password:
            issues.append("No uppercase letters")
        if not any(c.isdigit() for c in password):
            issues.append("No digits")
        return {
            "compliant": len(issues) == 0,
            "issues": issues,
            "score": max(0, 100 - len(issues) * 25),
        }

    def audit_file(self, path: str) -> Dict:
        with open(path, errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
        results = [self.check_nist(pw) for pw in passwords]
        compliant = sum(1 for r in results if r["compliant"])
        return {"total": len(results), "compliant": compliant, "non_compliant": len(results) - compliant}
