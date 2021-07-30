from typing import Any


class Urls:
    def __init__(self, item: Any):
        self._item = item

    @property
    def mini(self) -> str:
        return self._item["mini"]

    @property
    def original(self) -> str:
        return self._item["original"]

    @property
    def regular(self) -> str:
        return self._item["regular"]

    @property
    def small(self) -> str:
        return self._item["small"]

    @property
    def thumb(self) -> str:
        return self._item["thumb"]
