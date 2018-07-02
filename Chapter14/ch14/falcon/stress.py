from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
from time import time

N = 2500

URLS = ['http://127.0.0.1:8000/quote'] * N


def load_url(url, timeout):
    return urllib.request.urlopen(url, timeout=timeout).read()

start = time()
with ThreadPoolExecutor(max_workers=16) as executor:
    future_to_url = dict((executor.submit(load_url, url, 60), url)
                         for url in URLS)

    counter = 0
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        if future.exception() is not None:
            print('%r generated an exception: %s' % (
                url, future.exception())
            )
        else:
            counter += 1
            # print('%r page is %d bytes' % (
            #     url, len(future.result()))
            # )
            # print(future.result())

tot = time() - start
print(f'Rendered {N} pages in {tot:.3f} secs')
