from random import randint

import pytest

from ms.algo.mergesort_thread import sort as sort_thread
from ms.algo.mergesort_proc import sort as sort_proc


# the following helps when running $ pytest -vv tests
sort_thread.__name__ = 'Sort Thread'
sort_proc.__name__ = 'Sort Proc'


@pytest.fixture(params=[sort_thread, sort_proc])
def sort(request):
    return request.param


@pytest.fixture(params=list(range(1, 25)) + [10000])
def vector(request):
    yield [randint(-10**5, 10**5) for n in range(request.param)]


@pytest.fixture(params=[1, 2, 4, 8])
def workers(request):
    yield request.param


def test_random_vector(sort, vector, workers):
    assert sort(vector, workers=workers) == sorted(vector)


@pytest.mark.parametrize('v', [
    [],
    [1],
    [1, 1],
    [1, 2],
    [2, 1],
])
def test_sort_edge_cases(v, sort):
    sorted_v = sort(v)
    assert sorted_v == sorted(v)


def test_pure_function(sort):
    v = [2, 3, 1]
    idv = id(v)
    assert sort(v) == [1, 2, 3]
    assert id(v) == idv
    assert v == [2, 3, 1]
