from typing import TypedDict

import pytest

from pypixiv.client import PixivClient


class Filterd(TypedDict):
    obj: object
    name: str


def filter_magicmethod(obj: object) -> list[Filterd]:
    return [
        {"obj": obj, "name": property_name}
        for property_name in list(filter(lambda d: "_" not in d, dir(obj)))
    ]


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
