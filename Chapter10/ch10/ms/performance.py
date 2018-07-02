from time import time
from random import randint
from functools import partial
from contextlib import contextmanager

from algo.mergesort import sort
from algo.mergesort_thread import sort as sort_thread
from algo.mergesort_proc import sort as sort_proc


@contextmanager
def timer():
    t = time()
    yield
    tot = time() - t
    print(f'Elapsed time: {tot:.3f}s')


workers = 4
mx = 10 ** 7
sizes = [10 ** 5, 5 * 10 ** 5]
vectors = [
    [randint(-mx, mx) for _ in range(size)] for size in sizes
]


sort_th = partial(sort_thread, workers=workers)
sort_pr = partial(sort_proc, workers=workers)

sort.__name = 'Sort'
sort_th.__name = 'Sort Thread'
sort_pr.__name = 'Sort Proc'

for func in (sort, sort_th, sort_pr):
    print(f'Testing {func.__name}')
    for vector in vectors:
        items = len(vector)
        print(f'Size: {items}')
        with timer():
            func(vector)
    print()


"""
$ python performance.py

Testing Sort
Size: 100000
Elapsed time: 0.492s
Size: 500000
Elapsed time: 2.739s

Testing Sort Thread
Size: 100000
Elapsed time: 0.482s
Size: 500000
Elapsed time: 2.818s

Testing Sort Proc
Size: 100000
Elapsed time: 0.313s
Size: 500000
Elapsed time: 1.586s
"""
