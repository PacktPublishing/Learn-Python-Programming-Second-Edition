import threading


def sum_and_product(a, b):
    s, p = a + b, a * b
    print(f'{a}+{b}={s}, {a}*{b}={p}')


t = threading.Thread(
    target=sum_and_product, name='SumProd', args=(3, 7)
)
t.start()


"""
$ python start.py
3+7=10, 3*7=21
"""
