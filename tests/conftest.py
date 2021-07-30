import pytest

from pypixiv.client import PixivClient


@pytest.fixture()
async def client():
    client = PixivClient()
    yield client
    if client.session:
        await client.close()
