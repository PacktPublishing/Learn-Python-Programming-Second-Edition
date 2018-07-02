from random import randint

import pytest

from ms.algo.mergesort import sort


@pytest.fixture(params=list(range(1, 25)) + [10000])
def vector(request):
    yield [randint(-10**5, 10**5) for n in range(request.param)]


def test_random_vector(vector):
    assert sort(vector) == sorted(vector)


@pytest.mark.parametrize('v', [
    [],
    [1],
    [1, 1],
    [1, 2],
    [2, 1],
])
def test_sort_edge_cases(v):
    sorted_v = sort(v)
    assert sorted_v == sorted(v)


def test_pure_function():
    v = [2, 3, 1]
    idv = id(v)
    assert sort(v) == [1, 2, 3]
    assert id(v) == idv
    assert v == [2, 3, 1]
