from uuid import UUID

import httpx


class Manga:
    """Define MangaDex API wrapper."""

    def __init__(self, uuid: UUID):
        self.api = "https://api.mangadex.org/manga"
        self.uuid = uuid

    def exists(self):
        """Check if manga exists."""

        r = httpx.get(f"{self.api}/{self.uuid}")
        return r.status_code == 200
