"""Read hashcat/vulcan-crypt potfiles."""
import logging
from pathlib import Path
from typing import Dict

logger = logging.getLogger("specterhash.potfile")

class PotfileReader:
    def __init__(self, path: str = "~/.hashcat/hashcat.potfile"):
        self.path = Path(path).expanduser()
    def read(self) -> Dict[str, str]:
        entries = {}
        if not self.path.exists():
            logger.warning(f"Potfile not found: {self.path}")
            return entries
        with open(self.path) as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    h, p = line.split(":", 1)
                    entries[h] = p
        logger.info(f"Read {len(entries)} entries")
        return entries
