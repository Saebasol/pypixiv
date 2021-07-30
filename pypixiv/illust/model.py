from __future__ import annotations
from pypixiv.abc import BasePixiv

from pypixiv.illust.item import ZengoWorkData
from pypixiv.illust.body import IllustBody, UserIllustInfo
from typing import Any


class NoLoginData:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    # beadcrumbs

    @property
    def zengoIdWorks(self) -> list[UserIllustInfo]:
        return [UserIllustInfo(item) for item in self._item["zengoIdWorks"]]

    @property
    def zengoWorkData(self) -> ZengoWorkData:
        return ZengoWorkData(self._item["zengoWorkData"])


class IllustInfo(BasePixiv):
    def __init__(self, response: dict[str, Any]):
        super().__init__(response)

    @property
    def body(self) -> IllustBody:
        return IllustBody(super().body)
