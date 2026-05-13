"""Audit report generation."""
import json
import time
import logging
from typing import Dict, List
from pathlib import Path

logger = logging.getLogger("specterhash.report")

class ReportGenerator:
    """Generate audit reports."""

    def __init__(self, output_dir: str = "reports/"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, audit_results: Dict, format: str = "json") -> str:
        report = {
            "timestamp": time.time(),
            "summary": {
                "total_passwords": audit_results.get("total", 0),
                "compliant": audit_results.get("compliant", 0),
                "weak": audit_results.get("weak_count", 0),
                "avg_entropy": audit_results.get("avg_entropy", 0),
            },
            "details": audit_results.get("results", []),
        }
        path = self.output_dir / f"audit_{int(time.time())}.{format}"
        if format == "json":
            with open(path, "w") as f:
                json.dump(report, f, indent=2)
        logger.info(f"Report saved: {path}")
        return str(path)

    def summary_text(self, audit_results: Dict) -> str:
        lines = [
            "=" * 50,
            "SPECTERHASH AUDIT REPORT",
            "=" * 50,
            f"Total passwords: {audit_results.get('total', 0)}",
            f"Compliant: {audit_results.get('compliant', 0)}",
            f"Weak: {audit_results.get('weak_count', 0)}",
            f"Average entropy: {audit_results.get('avg_entropy', 0):.1f} bits",
            "=" * 50,
        ]
        return "\n".join(lines)
