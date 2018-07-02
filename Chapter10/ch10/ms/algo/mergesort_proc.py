from functools import reduce
from math import ceil
from concurrent.futures import ProcessPoolExecutor, as_completed

from .mergesort import sort as _sort, merge


def sort(v, workers=2):
    if len(v) == 0:
        return v

    dim = ceil(len(v) / workers)
    chunks = (v[k: k + dim] for k in range(0, len(v), dim))

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(_sort, chunk) for chunk in chunks
        ]
        return reduce(
            merge,
            (future.result() for future in as_completed(futures))
        )
