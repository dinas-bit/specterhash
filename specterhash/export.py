"""Export audit results in multiple formats."""
import csv
import json
import logging
from typing import List, Dict
from pathlib import Path

logger = logging.getLogger("specterhash.export")

class Exporter:
    def __init__(self, output_dir: str = "output/"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def to_csv(self, results: List[Dict], filename: str = "audit.csv"):
        path = self.output_dir / filename
        if not results: return
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        logger.info(f"Exported CSV: {path}")

    def to_json(self, results, filename="audit.json"):
        path = self.output_dir / filename
        with open(path, "w") as f:
            json.dump(results, f, indent=2)
        logger.info(f"Exported JSON: {path}")

    def to_txt(self, results, filename="audit.txt"):
        path = self.output_dir / filename
        with open(path, "w") as f:
            for r in results:
                f.write(f"{r}\n")
        logger.info(f"Exported TXT: {path}")
