from __future__ import annotations


from typing import Any, Optional


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


class TitleDesc:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    @property
    def description(self) -> str:
        return self._item["description"]

    @property
    def title(self) -> str:
        return self._item["title"]


class IdTitle:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    @property
    def id(self) -> str:
        return self._item["id"]

    @property
    def title(self) -> str:
        return self._item["title"]


class ZengoWorkData:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    @property
    def nextWork(self) -> IdTitle:
        return IdTitle(self._item["nextWork"])

    @property
    def prevWork(self) -> IdTitle:
        return IdTitle(self._item["prevWork"])


class Image(TitleDesc):
    def __init__(self, item: dict[str, Any]):
        super().__init__(item)

    @property
    def image(self) -> str:
        return self._item["image"]


class OGP(Image):
    def __init__(self, item: dict[str, Any]):
        super().__init__(item)

    @property
    def type(self) -> str:
        return self._item["type"]


class Twitter(Image):
    def __init__(self, item: dict[str, Any]):
        super().__init__(item)

    @property
    def card(self) -> str:
        return self._item["card"]


class Meta(TitleDesc):
    def __init__(self, item: dict[str, Any]):
        super().__init__(item)

    @property
    def alternateLanguages(self) -> list[Any]:
        return self._item["alternateLanguages"]

    @property
    def canonical(self) -> bool:
        return self._item["canonical"]

    @property
    def descriptionHeader(self) -> str:
        return self._item["descriptionHeader"]

    @property
    def ogp(self) -> Optional[OGP]:
        if "ogp" in self._item:
            return OGP(self._item["ogp"])

    @property
    def twitter(self) -> Optional[Twitter]:
        if "twitter" in self._item:
            return Twitter(self._item["twitter"])


class ExtraData:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    @property
    def meta(self) -> Optional[Meta]:
        if "meta" in self._item:
            return Meta(self._item["meta"])


class UserIdName:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    @property
    def userId(self) -> str:
        return self._item["userId"]

    @property
    def userName(self) -> str:
        return self._item["userName"]


class TagsInfo(UserIdName):
    def __init__(self, item: dict[str, Any]):
        super().__init__(item)

    @property
    def deletable(self) -> bool:
        return self._item["deletable"]

    @property
    def locked(self) -> bool:
        return self._item["locked"]

    @property
    def tag(self) -> str:
        return self._item["tag"]

    @property
    def translation(self) -> Optional[dict[str, str]]:
        if "translation" in self._item:
            return self._item["translation"]


class Tags:
    def __init__(self, item: dict[str, Any]):
        self.item = item

    @property
    def authorId(self) -> str:
        return self.item["authorId"]

    @property
    def isLocked(self) -> bool:
        return self.item["isLocked"]

    @property
    def tags(self) -> list[TagsInfo]:
        return [TagsInfo(i) for i in self.item["tags"]]

    @property
    def writable(self) -> bool:
        return self.item["writable"]
