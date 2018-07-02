import os
from secrets import token_hex
import asyncio

import aiohttp


PICS_FOLDER = 'pics'
URL = 'http://lorempixel.com/640/480/'
# URL = 'https://lorempizza.com/640/480/'


async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.read()


async def download(url, semaphore):
    async with semaphore:
        content = await download_image(url)
    filename = save_image(content)
    return filename


def save_image(content):
    filename = '{}.jpg'.format(token_hex(4))
    path = os.path.join(PICS_FOLDER, filename)
    with open(path, 'wb') as stream:
        stream.write(content)
    return filename


def batch_download(images, url):
    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(10)
    cors = [download(url, semaphore) for _ in range(images)]
    res, _ = loop.run_until_complete(asyncio.wait(cors))
    loop.close()
    return [r.result() for r in res]


if __name__ == '__main__':
    saved = batch_download(20, URL)
    print(saved)
