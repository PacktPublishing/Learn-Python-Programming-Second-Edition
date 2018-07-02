import os

import pytest

from sudoku.algo.solver import solve, solve_batch


@pytest.fixture
def puzzles_filename():
    return os.path.join('puzzles', 'sudoku-top95.txt')


def get_num(result):
    return int(result['A1'] + result['A2'] + result['A3'])


def test_solver(puzzles_filename):
    with open(puzzles_filename) as stream:
        results = [solve(puzzle.strip()) for puzzle in stream]
        s = sum(get_num(res) for res in results)
        assert s == 49074


def test_solver_batch(puzzles_filename):
    results = solve_batch(puzzles_filename, stats=False)
    s = sum(get_num(res) for res in results)
    assert s == 49074
