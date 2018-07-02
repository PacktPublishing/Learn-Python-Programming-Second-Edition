from random import randint

import pytest

from ms.algo.multi_mergesort import sort


@pytest.fixture(params=list(range(1, 25)) + [10000])
def vector(request):
    yield [randint(-10**5, 10**5) for n in range(request.param)]


@pytest.fixture(params=[2, 4, 8, 16])
def parts(request):
    yield request.param


def test_random_vector(vector, parts):
    assert sort(vector, parts=parts) == sorted(vector)


def test_at_least_two_parts():
    with pytest.raises(AssertionError) as err:
        sort([2, 7, 1], 1)

    assert err.match(r'Parts need to be at least 2\.')


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
