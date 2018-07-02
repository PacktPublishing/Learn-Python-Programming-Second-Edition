import os
from secrets import token_hex

import requests


PICS_FOLDER = 'pics'
URL = 'http://lorempixel.com/640/480/'
# URL = 'https://lorempizza.com/640/480/'


def download(url):
    resp = requests.get(URL)
    return save_image(resp.content)


def save_image(content):
    filename = '{}.jpg'.format(token_hex(4))
    path = os.path.join(PICS_FOLDER, filename)
    with open(path, 'wb') as stream:
        stream.write(content)
    return filename


def batch_download(url, n):
    return [download(url) for _ in range(n)]


if __name__ == '__main__':
    saved = batch_download(URL, 10)
    print(saved)
