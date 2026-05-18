"""Real-time monitoring dashboard."""
import time
import sys
from typing import Dict

class Dashboard:
    def __init__(self):
        self.start_time = time.time()
        self.stats = {"verified": 0, "cracked": 0, "weak": 0}

    def update(self, **kwargs):
        self.stats.update(kwargs)

    def render(self):
        elapsed = time.time() - self.start_time
        rate = self.stats["verified"] / max(elapsed, 0.001)
        lines = [
            "\033[2J\033[H",  # Clear screen
            "=" * 50,
            "  SPECTERHASH LIVE DASHBOARD",
            "=" * 50,
            f"  Elapsed:   {elapsed:.0f}s",
            f"  Verified:  {self.stats['verified']:,}",
            f"  Cracked:   {self.stats['cracked']:,}",
            f"  Weak:      {self.stats['weak']:,}",
            f"  Rate:      {rate:,.0f}/s",
            "=" * 50,
        ]
        sys.stderr.write("\n".join(lines) + "\n")
        sys.stderr.flush()
