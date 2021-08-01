from pypixiv.ranking.item import IllustContentType
from typing import Any


class ContentBody:
    def __init__(self, response: Any) -> None:
        self._response = response

    @property
    def title(self) -> str:
        return self._response["title"]

    @property
    def date(self) -> str:
        return self._response["date"]

    @property
    def tags(self) -> list[str]:
        return self._response["tags"]

    @property
    def url(self) -> str:
        return self._response["url"]

    @property
    def illust_type(self) -> str:
        return self._response["illust_type"]

    @property
    def illust_book_style(self) -> str:
        return self._response["illust_book_style"]

    @property
    def illust_page_count(self) -> int:
        return self._response["illust_page_count"]

    @property
    def user_name(self) -> str:
        return self._response["user_name"]

    @property
    def profile_img(self) -> str:
        return self._response["profile_img"]

    @property
    def illust_content_type(self) -> IllustContentType:
        return IllustContentType(self._response["illust_content_type"])

    @property
    def illust_series(self) -> bool:
        return self._response["illust_series"]

    @property
    def illust_id(self) -> int:
        return self._response["illust_id"]

    @property
    def width(self) -> int:
        return self._response["width"]

    @property
    def height(self) -> int:
        return self._response["height"]

    @property
    def user_id(self) -> int:
        return self._response["user_id"]

    @property
    def rank(self) -> int:
        return self._response["rank"]

    @property
    def yes_rank(self) -> int:
        return self._response["yes_rank"]

    @property
    def rating_count(self) -> int:
        return self._response["rating_count"]

    @property
    def view_count(self) -> int:
        return self._response["view_count"]

    @property
    def illust_upload_timestamp(self) -> int:
        return self._response["illust_upload_timestamp"]

    @property
    def attr(self) -> str:
        return self._response["attr"]

    @property
    def is_bookmarked(self) -> bool:
        return self._response["is_bookmarked"]

    @property
    def bookmarkable(self) -> bool:
        return self._response["bookmarkable"]
