import threading
from time import sleep


class Fibo(threading.Thread):

    def __init__(self, *a, **kwa):
        super().__init__(*a, **kwa)
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        a, b = 0, 1
        while self._running:
            print(a, end=' ')
            a, b = b, a + b
            sleep(0.07)
        print()


fibo = Fibo()
fibo.start()
sleep(1)
fibo.stop()
fibo.join()

print('All done.')


"""
$ python stop.py
0 1 1 2 3 5 8 13 21 34 55 89 144 233
All done.
"""
