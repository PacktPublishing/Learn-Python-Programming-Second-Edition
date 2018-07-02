import multiprocessing


SENTINEL = 'STOP'


def producer(q, n):
    a, b = 0, 1
    while a <= n:
        q.put(a)
        a, b = b, a + b
    q.put(SENTINEL)


def consumer(q):
    while True:
        num = q.get()
        if num == SENTINEL:
            break
        print(f'Got number {num}')


q = multiprocessing.Queue()
cns = multiprocessing.Process(target=consumer, args=(q, ))
prd = multiprocessing.Process(target=producer, args=(q, 35))

cns.start()
prd.start()

"""
$ python comm_queue_proc.py
Got number 0
Got number 1
Got number 1
Got number 2
Got number 3
Got number 5
Got number 8
Got number 13
Got number 21
Got number 34
"""
