"""Secure password generation."""
import secrets
import string
import logging
from typing import Optional

logger = logging.getLogger("specterhash.generator")

class PasswordGenerator:
    """Generate cryptographically secure passwords."""

    def __init__(self, length: int = 16, use_upper: bool = True, use_digits: bool = True,
                 use_special: bool = True, exclude_ambiguous: bool = False):
        self.length = length
        charset = string.ascii_lowercase
        if use_upper: charset += string.ascii_uppercase
        if use_digits: charset += string.digits
        if use_special: charset += "!@#$%^&*()-_+="
        if exclude_ambiguous:
            charset = charset.replace("0", "").replace("O", "").replace("l", "").replace("1", "").replace("I", "")
        self.charset = charset

    def generate(self) -> str:
        return "".join(secrets.choice(self.charset) for _ in range(self.length))

    def generate_batch(self, count: int) -> list:
        return [self.generate() for _ in range(count)]

    def generate_passphrase(self, word_count: int = 4, separator: str = "-") -> str:
        words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf",
                 "hotel", "india", "juliet", "kilo", "lima", "mike", "november",
                 "oscar", "papa", "quebec", "romeo", "sierra", "tango"]
        return separator.join(secrets.choice(words) for _ in range(word_count))
