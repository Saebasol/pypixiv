import pytest

from pypixiv.client import PixivClient
from tests.util import filter_magicmethod


@pytest.mark.asyncio
async def test_illustinfo(client: PixivClient):
    user = await client.illustinfo(79136250)
    property_names = filter_magicmethod(user)

    for i in property_names:
        getted = getattr(i["obj"], i["name"])
        if not type(getted).__module__ in ["__builtin__", "builtins"]:
            if son := filter_magicmethod(getted):
                property_names.extend(son)
