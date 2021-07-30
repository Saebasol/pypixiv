from typing import Any, Optional


class Privacy:
    def __init__(self, item: Any):
        self.__item = item

    @property
    def name(self) -> Optional[str]:
        return self.__item["name"]

    @property
    def privacyLeve(self) -> Optional[bool]:
        return self.__item["privacyLevel"]


class SketchLives:
    def __init__(self, item: Any):
        self.__item = item

    @property
    def audienceCount(self) -> Optional[int]:
        return self.__item["audienceCount"]

    @property
    def id(self) -> Optional[str]:
        return self.__item["id"]

    @property
    def isR18(self) -> Optional[bool]:
        return self.__item["isR18"]

    @property
    def name(self) -> Optional[str]:
        return self.__item["name"]

    @property
    def streamerIds(self) -> Optional[list[int]]:
        return self.__item["streamerIds"]

    @property
    def thumbnailUrl(self) -> Optional[str]:
        return self.__item["thumbnailUrl"]

    @property
    def url(self) -> Optional[str]:
        return self.__item["url"]


class Group:
    def __init__(self, item: Any):
        self.__item = item

    @property
    def iconUrl(self) -> Optional[str]:
        return self.__item["iconUrl"]

    @property
    def id(self) -> Optional[str]:
        return self.__item["id"]

    @property
    def title(self) -> Optional[str]:
        return self.__item["title"]


class SocialUrl:
    def __init__(self, item: Any):
        self.__item = item

    @property
    def url(self) -> Optional[str]:
        return self.__item["url"]


class Pawoo(SocialUrl):
    def __init__(self, item: Any):
        super().__init__(item)


class Twitter(SocialUrl):
    def __init__(self, item: Any):
        super().__init__(item)


class Social:
    def __init__(self, item: Any):
        self.__item = item

    @property
    def pawoo(self) -> Optional[Pawoo]:
        if "pawoo" in self.__item:
            return Pawoo(self.__item["pawoo"])

    @property
    def twitter(self) -> Optional[Twitter]:
        if "twitter" in self.__item:
            return Twitter(self.__item["twitter"])


class WorkSpace:
    def __init__(self, item: Any):
        self.__item = item

    @property
    def userWorkspaceChair(self) -> Optional[str]:
        return self.__item.get("userWorkspaceChair")

    @property
    def userWorkspaceComment(self) -> Optional[str]:
        return self.__item.get("userWorkspaceComment")

    @property
    def userWorkspaceDesk(self) -> Optional[str]:
        return self.__item.get("userWorkspaceDesk")

    @property
    def userWorkspaceDesktop(self) -> Optional[str]:
        return self.__item.get("userWorkspaceDesktop")

    @property
    def userWorkspaceMonitor(self) -> Optional[str]:
        return self.__item.get("userWorkspaceMonitor")

    @property
    def userWorkspaceMouse(self) -> Optional[str]:
        return self.__item.get("userWorkspaceMouse")

    @property
    def userWorkspacePc(self) -> Optional[str]:
        return self.__item.get("userWorkspacePc")

    @property
    def userWorkspacePrinter(self) -> Optional[str]:
        return self.__item.get("userWorkspacePrinter")

    @property
    def userWorkspaceScanner(self) -> Optional[str]:
        return self.__item.get("userWorkspaceScanner")

    @property
    def userWorkspaceTablet(self) -> Optional[str]:
        return self.__item.get("userWorkspaceTablet")

    @property
    def userWorkspaceTool(self) -> Optional[str]:
        return self.__item.get("userWorkspaceTool")

    @property
    def wsBigUrl(self) -> Optional[str]:
        return self.__item.get("wsBigUrl")

    @property
    def wsUrl(self) -> Optional[str]:
        return self.__item.get("wsUrl")
