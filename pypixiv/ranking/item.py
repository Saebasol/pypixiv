from typing import Any


class IllustContentType:
    def __init__(self, item: Any) -> None:
        self.__item = item

    @property
    def sexual(self) -> int:
        return self.__item["sexual"]

    @property
    def lo(self) -> bool:
        return self.__item["lo"]

    @property
    def grotesque(self) -> bool:
        return self.__item["grotesque"]

    @property
    def violent(self) -> bool:
        return self.__item["violent"]

    @property
    def homosexual(self) -> bool:
        return self.__item["homosexual"]

    @property
    def drug(self) -> bool:
        return self.__item["drug"]

    @property
    def thoughts(self) -> bool:
        return self.__item["thoughts"]

    @property
    def antisocial(self) -> bool:
        return self.__item["antisocial"]

    @property
    def religion(self) -> bool:
        return self.__item["religion"]

    @property
    def original(self) -> bool:
        return self.__item["original"]

    @property
    def furry(self) -> bool:
        return self.__item["furry"]

    @property
    def bl(self) -> bool:
        return self.__item["bl"]

    @property
    def yuri(self) -> bool:
        return self.__item["yuri"]
