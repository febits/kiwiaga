from pathlib import Path
from typing import Dict, List
from uuid import UUID

import yaml

from kiwiaga import __configpath__


class Config:
    """Define config wrapper to yaml stuff."""

    def __init__(self):
        self.template = {"mangas": []}
        self.path = Path(__configpath__)
        self.yaml = {}

    def write(self, data: Dict[str, List[UUID]]):
        """Write data to path."""

        if not self.path.exists():
            self.path.touch(mode=0o644)

        with self.path.open("w", encoding="utf-8") as f:
            yaml.dump(data, f)

    def read(self):
        """Read from path to yaml."""

        with self.path.open("r", encoding="utf-8") as f:
            self.yaml = yaml.safe_load(f)
