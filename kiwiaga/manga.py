from uuid import UUID

import httpx


class Manga:
    """Define MangaDex API wrapper."""

    def __init__(self, uuid: UUID, language: str | None = "en"):
        self.api = "https://api.mangadex.org/manga"
        self.api_params = {
            "includeFuturePublishAt": 0,
            "order[chapter]": "desc",
            "translatedLanguage[]": [language],
            "limit": 1,
        }
        self.uuid = uuid
        self.name = ""
        self.lastchap_title = ""
        self.lastchap_publish_at = ""
        self.lastchap = ""

    def exists(self):
        """Check if manga exists."""

        r = httpx.get(f"{self.api}/{self.uuid}")
        return r.status_code == 200

    def get_info(self):
        """Get info about manga."""

        manga_name = httpx.get(f"{self.api}/{self.uuid}")
        lastchap = httpx.get(f"{self.api}/{self.uuid}/feed", params=self.api_params)

        if manga_name.status_code == 200:
            self.name = manga_name.json()["data"]["attributes"]["title"]["en"]

            if lastchap.status_code == 200 and lastchap.json()["data"]:
                self.lastchap_title = lastchap.json()["data"][0]["attributes"]["title"]
                self.lastchap_publish_at = lastchap.json()["data"][0]["attributes"][
                    "publishAt"
                ]
                self.lastchap = lastchap.json()["data"][0]["attributes"]["chapter"]

                return True

            return False

        return False
