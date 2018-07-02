
def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_hypotenuse(a, b):
    return (a**2 + b**2) ** .5


def is_int(n):  # n is expected to be a float
    return n.is_integer()


triples = calc_triples(1000)

"""
$ python -m cProfile triples.py
1502538 function calls in 0.704 seconds

Ordered by: standard name

ncalls  tottime  percall  filename:lineno(function)
500500    0.393    0.000  triples.py:17(calc_hypotenuse)
500500    0.096    0.000  triples.py:21(is_int)
     1    0.000    0.000  triples.py:4(<module>)
     1    0.176    0.176  triples.py:4(calc_triples)
     1    0.000    0.000  {built-in method builtins.exec}
  1034    0.000    0.000  {method 'append' of 'list' objects}
     1    0.000    0.000  {method 'disable' of '_lsprof.Profil...
500500    0.038    0.000  {method 'is_integer' of 'float' objects}
"""
