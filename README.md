# pypixiv

> Pixiv ajax python wrapper

## Feature

* Asynchronous.

* Fully type annotated.

* The response is returned as an object.

## Simple Example

```py
import asyncio

from pypixiv.client import PixivClient


async def main():
    async with PixivClient() as client:
        illust = await client.illustinfo(79136250)
        user_id = int(illust.userId)
        print(user_id)
        user = await client.userinfo(id)
        print(user.name)


asyncio.run(main())
```
