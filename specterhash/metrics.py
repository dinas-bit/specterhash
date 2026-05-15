"""Prometheus metrics."""
import time
from typing import Dict

class Metrics:
    def __init__(self):
        self.counters: Dict[str, int] = {}
        self.gauges: Dict[str, float] = {}
    def inc(self, name, v=1):
        self.counters[name] = self.counters.get(name, 0) + v
    def gauge(self, name, v):
        self.gauges[name] = v
    def export(self) -> str:
        lines = []
        for k, v in self.counters.items():
            lines.append(f"specterhash_{k} {v}")
        for k, v in self.gauges.items():
            lines.append(f"specterhash_{k} {v}")
        return "\n".join(lines) + "\n"

metrics = Metrics()
