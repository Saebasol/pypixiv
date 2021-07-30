from pypixiv.user.item import Group, Privacy, SketchLives, WorkSpace
from typing import Any, Optional


class UserInfoBody:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def acceptRequest(self) -> bool:
        return self._response["acceptRequest"]

    @property
    def background(self) -> Optional[str]:
        return self._response["background"]

    @property
    def image(self) -> Optional[str]:
        return self._response["image"]

    @property
    def imageBig(self) -> Optional[str]:
        return self._response["imageBig"]

    @property
    def isBlocking(self) -> bool:
        return self._response["isBlocking"]

    @property
    def isFollowed(self) -> bool:
        return self._response["isFollowed"]

    @property
    def isMypixiv(self) -> bool:
        return self._response["isMypixiv"]

    @property
    def name(self) -> Optional[str]:
        return self._response["name"]

    @property
    def partial(self) -> int:
        return self._response["partial"]

    @property
    def premium(self) -> bool:
        return self._response["premium"]

    @property
    def sketchLiveId(self) -> Optional[str]:
        return self._response["sketchLiveId"]

    @property
    def sketchLives(self) -> list[SketchLives]:
        return [SketchLives(item) for item in self._response["sketchLives"]]


class UserFullInfoBody(UserInfoBody):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def birthDay(self) -> Privacy:
        return Privacy(self._response["birthDay"])

    @property
    def userId(self) -> str:
        return self._response["userId"]

    @property
    def commment(self) -> Optional[str]:
        return self._response["comment"]

    @property
    def commentHtml(self) -> Optional[str]:
        return self._response["commentHtml"]

    @property
    def followedBack(self) -> bool:
        return self._response["followedBack"]

    @property
    def following(self) -> int:
        return self._response["following"]

    @property
    def gender(self) -> Privacy:
        return Privacy(self._response["gender"])

    @property
    def group(self) -> Optional[list[Group]]:
        if group := self._response.get("group"):
            return [Group(item) for item in group]

    @property
    def job(self) -> Privacy:
        return Privacy(self._response["job"])

    @property
    def official(self) -> bool:
        return self._response["official"]

    @property
    def region(self) -> Privacy:
        return Privacy(self._response["region"])

    @property
    def workspace(self) -> WorkSpace:
        return WorkSpace(self._response["workspace"])
