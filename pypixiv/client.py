from typing import Optional

from aiohttp.client import ClientSession

from pypixiv.http import PixivHttpClient
from pypixiv.models.illust import IllustInfo
from pypixiv.models.user import UserFullInfo, UserInfo


class PixivClient(PixivHttpClient):
    """
    Pixiv API client class.
    """

    def __init__(
        self, session: Optional[ClientSession] = None, lang: str = "ko"
    ) -> None:
        super().__init__(session=session, lang=lang)

    async def userinfo(self, user_id: int):
        return UserInfo(await self.get_userinfo(user_id))

    async def full_userinfo(self, user_id: int):
        return UserFullInfo(await self.get_full_userinfo(user_id))

    async def illustinfo(self, illust_id: int):
        return IllustInfo(await self.get_illust(illust_id))
