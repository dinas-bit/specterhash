"""Configuration."""
DEFAULT = {
    "specterhash": {"device_id": 0, "log_level": "info"},
    "audit": {"min_length": 8, "check_breach": True},
}

class Config:
    def __init__(self): self.data = DEFAULT.copy()
    def load(self): return self.data
    def get(self, k, d=None):
        v = self.data
        for p in k.split("."):
            if isinstance(v, dict) and p in v: v = v[p]
            else: return d
        return v
