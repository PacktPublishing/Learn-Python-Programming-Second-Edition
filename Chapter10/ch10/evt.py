import threading


def fire():
    print('Firing event...')
    event.set()


def listen():
    event.wait()
    print('Event has been fired')


event = threading.Event()
t1 = threading.Thread(target=fire)
t2 = threading.Thread(target=listen)
t2.start()
t1.start()

"""
$ python evt.py
Firing event...
Event has been fired
"""
