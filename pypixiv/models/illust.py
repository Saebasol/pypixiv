from __future__ import annotations
from pypixiv.models.url import Urls

from typing import Any, Optional

from pypixiv.models.abc import BaseDictPixiv


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

    # TODO: Check this type
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


class BaseInfo(BaseDictPixiv):
    def __init__(self, response: Any):
        super().__init__(response)

    @property
    def pageCount(self) -> int:
        return self.body["pageCount"]

    @property
    def restrict(self) -> int:
        return self.body["restrict"]

    @property
    def sl(self) -> int:
        return self.body["sl"]


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


class ShortIllustInfo(BaseInfo, UserIdName):
    def __init__(self, response: Any) -> None:
        BaseInfo.__init__(self, response)
        UserIdName.__init__(self, response.get("body") or response)

    def __repr__(self) -> str:
        return f"<title={self.title}>"

    @property
    def alt(self) -> str:
        return self.body["alt"]

    @property
    def bookMarkData(self) -> str:
        return self.body["bookmarkData"]

    @property
    def createDate(self) -> str:
        return self.body["createDate"]

    @property
    def description(self) -> str:
        return self.body["description"]

    @property
    def height(self) -> int:
        return self.body["height"]

    @property
    def id(self) -> str:
        return self.body["id"]

    @property
    def illustType(self) -> int:
        return self.body["illustType"]

    @property
    def isBookmarkable(self) -> str:
        return self.body["isBookmarkable"]

    @property
    def isUnlisted(self) -> str:
        return self.body["isUnlisted"]

    @property
    def title(self) -> str:
        return self.body["title"]

    @property
    def titleCaptionTranslation(self) -> str:
        return self.body["titleCaptionTranslation"]

    @property
    def width(self) -> int:
        return self.body["width"]

    @property
    def xRestrict(self) -> int:
        return self.body["xRestrict"]


class SingleTagsShortIllustInfo(ShortIllustInfo):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def url(self) -> str:
        return self.body["url"]

    @property
    def profileImageUrl(self) -> str:
        return self.body["profileImageUrl"]

    @property
    def isMasked(self) -> Optional[str]:
        return self.body["isMasked"]

    @property
    def tags(self) -> list[str]:
        return self.body["tags"]

    @property
    def updateDate(self) -> str:
        return self.body["updateDate"]


class NoLoginData:
    def __init__(self, item: dict[str, Any]):
        self._item = item

    # beadcrumbs

    @property
    def zengoIdWorks(self) -> list[ShortIllustInfo]:
        return [ShortIllustInfo(item) for item in self._item["zengoIdWorks"]]

    @property
    def zengoWorkData(self) -> ZengoWorkData:
        return ZengoWorkData(self._item["zengoWorkData"])


class IllustInfo(ShortIllustInfo):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def bookmarkCount(self) -> int:
        return self.body["bookmarkCount"]

    @property
    def comicPromotion(self) -> bool:
        return self.body["comicPromotion"]

    @property
    def commentCount(self) -> int:
        return self.body["commentCount"]

    @property
    def contestBanners(self) -> list[str]:
        return self.body["contestBanners"]

    @property
    def contestData(self) -> Optional[str]:
        return self.body["contestData"]

    @property
    def descriptionBoothId(self) -> Optional[str]:
        return self.body["descriptionBoothId"]

    @property
    def descriptionYoutubeId(self) -> Optional[str]:
        return self.body["descriptionYoutubeId"]

    @property
    def extraData(self) -> Optional[ExtraData]:
        if "extraData" in self.body:
            return ExtraData(self.body["extraData"])
        return

    @property
    def fanboxPromotion(self) -> Any:
        return self.body["fanboxPromotion"]

    @property
    def illustComment(self) -> str:
        return self.body["illustComment"]

    @property
    def illustTitle(self) -> str:
        return self.body["illustTitle"]

    @property
    def imageResponseCount(self) -> int:
        return self.body["imageResponseCount"]

    @property
    def imageResponseData(self) -> Any:
        return self.body["imageResponseData"]

    @property
    def imageResponseOutData(self) -> Any:
        return self.body["imageResponseOutData"]

    @property
    def isHowto(self) -> bool:
        return self.body["isHowto"]

    @property
    def isOriginal(self) -> bool:
        return self.body["isOriginal"]

    @property
    def likeCount(self) -> int:
        return self.body["likeCount"]

    @property
    def likeData(self) -> Any:
        return self.body["likeData"]

    @property
    def noLoginData(self) -> Optional[NoLoginData]:
        if "noLoginData" in self.body:
            return NoLoginData(self.body["noLoginData"])

    @property
    def pollData(self) -> Optional[Any]:
        return self.body["pollData"]

    @property
    def request(self) -> Any:
        return self.body["request"]

    @property
    def responseCount(self) -> int:
        return self.body["responseCount"]

    @property
    def seriesNavData(self) -> Optional[Any]:
        return self.body["seriesNavData"]

    @property
    def storableTags(self) -> list[str]:
        return self.body["storableTags"]

    @property
    def tags(self) -> Tags:
        return Tags(self.body["tags"])

    @property
    def urls(self) -> Urls:
        return Urls(self.body["urls"])

    @property
    def userAccount(self) -> str:
        return self.body["userAccount"]

    @property
    def viewCount(self) -> int:
        return self.body["viewCount"]

    @property
    def userIllusts(self) -> list[SingleTagsShortIllustInfo | int]:
        return [
            SingleTagsShortIllustInfo(self.body["userIllusts"][k])
            if self.body["userIllusts"][k]
            else k
            for k in self.body["userIllusts"].keys()
        ]
