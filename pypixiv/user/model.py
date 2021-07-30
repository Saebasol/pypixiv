from pypixiv.user.body import UserFullInfoBody, UserInfoBody
from typing import Any
from pypixiv.abc import BasePixiv


class UserInfo(BasePixiv):
    def __init__(self, response: Any):
        super().__init__(response)

    @property
    def body(self) -> UserInfoBody:
        return UserInfoBody(super().body)


class UserFullInfo(BasePixiv):
    def __init__(self, response: Any):
        super().__init__(response)

    @property
    def body(self) -> UserFullInfoBody:
        return UserFullInfoBody(super().body)
