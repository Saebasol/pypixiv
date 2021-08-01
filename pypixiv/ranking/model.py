from pypixiv.ranking.body import ContentBody
from typing import Any
from pypixiv.abc import BaseRanking


class RankingInfo(BaseRanking):
    def __init__(self, response: Any):
        super().__init__(response)

    @property
    def contents(self) -> list[ContentBody]:
        return [ContentBody(content) for content in self.response["contents"]]
