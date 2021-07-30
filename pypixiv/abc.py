from __future__ import annotations

from typing import Any


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
