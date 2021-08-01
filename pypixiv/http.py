from types import TracebackType
from typing import Any, Literal, Optional

from aiohttp import ClientSession


class PixivHttpClient:
    API_URL = "https://www.pixiv.net"

    def __init__(
        self, session: Optional[ClientSession] = None, lang: str = "ko"
    ) -> None:
        self.session = session
        self.lang = lang

    @property
    def headers(self) -> dict[str, str]:
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Referer": self.API_URL,
        }

    @headers.setter
    def headers(self, value: dict[str, str]) -> None:
        self.headers.update(value)

    @property
    def params(self) -> dict[str, Any]:
        return {"lang": self.lang}

    @params.setter
    def params(self, value: dict[str, Any]) -> None:
        self.params.update(value)

    async def close(self):
        if self.session:
            await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ):
        await self.close()

    async def request(
        self, method: Literal["GET", "POST"], path: str, **kwargs: Any
    ) -> Any:
        if not self.session:
            self.session = ClientSession(headers=self.headers)

        async with self.session.request(
            method, f"{self.API_URL}/ajax/{path}", **kwargs
        ) as r:
            return await r.json()

    async def get_userinfo(self, user_id: int) -> Any:
        params = {"full": 0, **self.params}
        return await self.request("GET", f"user/{user_id}", params=params)

    async def get_full_userinfo(self, user_id: int) -> Any:
        params = {"full": 1, **self.params}
        return await self.request("GET", f"user/{user_id}", params=params)

    async def get_illust(self, illust_id: int) -> Any:
        params = {**self.params}
        return await self.request("GET", f"illust/{illust_id}", params=params)

    async def get_ranking(
        self,
        mode: Literal["dailly", "weekly", "monthly"] = "dailly",
        date: Optional[int] = None,
    ) -> Any:
        params = {"format": "json", "mode": mode}
        if date:
            params.update({"date": date})

        return await self.request("GET", "ranking", params=params)
