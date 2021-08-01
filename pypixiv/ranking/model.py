from typing import Any
from typing import List

from pypixiv.abc import BaseRanking
from pypixiv.ranking.body import ContentBody


class RankingInfo(BaseRanking):
    def __init__(self, response: Any):
        super().__init__(response)

    @property
    def contents(self) -> List[ContentBody]:
        return [ContentBody(content) for content in self.response["contents"]]
