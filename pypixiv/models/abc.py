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
    def body(self) -> dict[str, Any] | list[dict[str, Any]]:
        return self.__response["body"]


class BaseDictPixiv(BasePixiv):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def body(self) -> dict[str, Any]:
        body = super().body
        assert isinstance(body, dict)
        return body


class BaseListPixiv(BasePixiv):
    def __init__(self, response: Any) -> None:
        super().__init__(response)

    @property
    def body(self) -> list[dict[str, Any]]:
        body = super().body
        assert isinstance(body, list)
        return body
