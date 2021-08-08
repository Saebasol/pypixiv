import pytest

from pypixiv.client import PixivClient

from tests.util import filter_magicmethod


@pytest.mark.asyncio
async def test_userinfo(client: PixivClient):
    user = await client.userinfo(9666585)
    property_names = filter_magicmethod(user)

    for i in property_names:
        getted = getattr(i["obj"], i["name"])
        if not type(getted).__module__ in ["__builtin__", "builtins"]:
            if son := filter_magicmethod(getted):
                property_names.extend(son)


@pytest.mark.asyncio
async def test_full_userinfo(client: PixivClient):
    user = await client.userinfo(9666585)
    property_names = filter_magicmethod(user)

    for i in property_names:
        getted = getattr(i["obj"], i["name"])
        if not type(getted).__module__ in ["__builtin__", "builtins"]:
            if son := filter_magicmethod(getted):
                property_names.extend(son)
