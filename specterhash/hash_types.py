"""Hash type definitions."""
from enum import Enum

class HashType(Enum):
    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"
    BCRYPT = "bcrypt"
    ARGON2 = "argon2"
    NTLM = "ntlm"

def detect_hash(h: str) -> HashType:
    if h.startswith("$2"): return HashType.BCRYPT
    if h.startswith("$argon2"): return HashType.ARGON2
    length = len(h)
    if length == 32: return HashType.MD5
    if length == 40: return HashType.SHA1
    if length == 64: return HashType.SHA256
    if length == 128: return HashType.SHA512
    return HashType.MD5
