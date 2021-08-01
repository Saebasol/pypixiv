from __future__ import annotations

from typing import Any, Union


class BasePixiv:
    # error: str
    # message: str
    # body: dict[str, Any] | list[dict[str, Any]]

    def __init__(self, response: Any) -> None:
        self.__response = response

    @property
    def error(self) -> str:
        return self.__response["error"]

    @property
    def message(self) -> str:
        return self.__response["message"]

    @property
    def body(self) -> Any:
        return self.__response["body"]


class BaseRanking:
    def __init__(self, response: Any) -> None:
        self.__response = response

    @property
    def contents(self) -> list[dict[str, Any]]:
        return self.__response["contents"]

    @property
    def mode(self) -> str:
        return self.__response["mode"]

    @property
    def content(self) -> str:
        return self.__response["content"]

    @property
    def page(self) -> int:
        return self.__response["page"]

    @property
    def prev(self) -> bool:
        return self.__response["prev"]

    @property
    def next(self) -> int:
        return self.__response["next"]

    @property
    def date(self) -> str:
        return self.__response["date"]

    @property
    def prev_date(self) -> str:
        return self.__response["prev_date"]

    @property
    def next_date(self) -> Union[str, bool]:
        return self.__response["next_date"]

    @property
    def rank_total(self) -> int:
        return self.__response["rank_total"]
