from pypixiv.illust.item import ExtraData, Tags, Urls
from typing import Any, Optional


class DefaultIllustInfo:
    def __init__(self, response: Any) -> None:
        self._response = response

    def __repr__(self) -> str:
        return f"<title={self.title}>"

    @property
    def alt(self) -> str:
        return self._response["alt"]

    @property
    def bookMarkData(self) -> str:
        return self._response["bookmarkData"]

    @property
    def createDate(self) -> str:
        return self._response["createDate"]

    @property
    def description(self) -> str:
        return self._response["description"]

    @property
    def height(self) -> int:
        return self._response["height"]

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def illustType(self) -> int:
        return self._response["illustType"]

    @property
    def isBookmarkable(self) -> str:
        return self._response["isBookmarkable"]

    @property
    def isUnlisted(self) -> str:
        return self._response["isUnlisted"]

    @property
    def title(self) -> str:
        return self._response["title"]

    @property
    def titleCaptionTranslation(self) -> str:
        return self._response["titleCaptionTranslation"]

    @property
    def width(self) -> int:
        return self._response["width"]

    @property
    def xRestrict(self) -> int:
        return self._response["xRestrict"]

    @property
    def pageCount(self) -> int:
        return self._response["pageCount"]

    @property
    def restrict(self) -> int:
        return self._response["restrict"]

    @property
    def sl(self) -> int:
        return self._response["sl"]


class UserIllustInfo(DefaultIllustInfo):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def url(self) -> str:
        return self._response["url"]

    @property
    def profileImageUrl(self) -> str:
        return self._response["profileImageUrl"]

    @property
    def isMasked(self) -> Optional[str]:
        return self._response["isMasked"]

    @property
    def tags(self) -> list[str]:
        return self._response["tags"]

    @property
    def updateDate(self) -> str:
        return self._response["updateDate"]


class IllustBody(DefaultIllustInfo):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def bookmarkCount(self) -> int:
        return self._response["bookmarkCount"]

    @property
    def comicPromotion(self) -> bool:
        return self._response["comicPromotion"]

    @property
    def commentCount(self) -> int:
        return self._response["commentCount"]

    @property
    def contestBanners(self) -> list[str]:
        return self._response["contestBanners"]

    @property
    def contestData(self) -> Optional[str]:
        return self._response["contestData"]

    @property
    def descriptionBoothId(self) -> Optional[str]:
        return self._response["descriptionBoothId"]

    @property
    def descriptionYoutubeId(self) -> Optional[str]:
        return self._response["descriptionYoutubeId"]

    @property
    def extraData(self) -> Optional[ExtraData]:
        if "extraData" in self._response:
            return ExtraData(self._response["extraData"])
        return

    @property
    def fanboxPromotion(self) -> Any:
        return self._response["fanboxPromotion"]

    @property
    def illustComment(self) -> str:
        return self._response["illustComment"]

    @property
    def illustTitle(self) -> str:
        return self._response["illustTitle"]

    @property
    def imageResponseCount(self) -> int:
        return self._response["imageResponseCount"]

    @property
    def imageResponseData(self) -> Any:
        return self._response["imageResponseData"]

    @property
    def imageResponseOutData(self) -> Any:
        return self._response["imageResponseOutData"]

    @property
    def isHowto(self) -> bool:
        return self._response["isHowto"]

    @property
    def isOriginal(self) -> bool:
        return self._response["isOriginal"]

    @property
    def likeCount(self) -> int:
        return self._response["likeCount"]

    @property
    def likeData(self) -> Any:
        return self._response["likeData"]

    @property
    def pollData(self) -> Optional[Any]:
        return self._response["pollData"]

    @property
    def request(self) -> Any:
        return self._response["request"]

    @property
    def responseCount(self) -> int:
        return self._response["responseCount"]

    @property
    def seriesNavData(self) -> Optional[Any]:
        return self._response["seriesNavData"]

    @property
    def storableTags(self) -> list[str]:
        return self._response["storableTags"]

    @property
    def tags(self) -> Tags:
        return Tags(self._response["tags"])

    @property
    def urls(self) -> Urls:
        return Urls(self._response["urls"])

    @property
    def userAccount(self) -> str:
        return self._response["userAccount"]

    @property
    def viewCount(self) -> int:
        return self._response["viewCount"]
