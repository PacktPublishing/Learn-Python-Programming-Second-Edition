"""

This sudoku solver is an adaptation from Peter Norvig's original
implementation. You can find his code in the `norvig` folder.
This version introduces a couple of small simplifications, and
exhibit a slightly better choice of names, which was necessary in
order to present the code in the book and be able to explain it
more easily.

"""
import os
from itertools import zip_longest, chain
from time import time


def cross_product(v1, v2):
    return [w1 + w2 for w1 in v1 for w2 in v2]


def chunk(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross_product(rows, cols)
all_units = (
    [cross_product(rows, c) for c in cols]
    + [cross_product(r, cols) for r in rows]
    + [cross_product(rs, cs)
        for rs in chunk(rows, 3) for cs in chunk(cols, 3)]
)
units = dict(
    (square, [unit for unit in all_units if square in unit])
    for square in squares
)
peers = dict(
    (square, set(chain(*units[square])) - set([square]))
    for square in squares
)


def parse_puzzle(puzzle):
    assert set(puzzle) <= set('.0123456789')
    assert len(puzzle) == 81

    grid = dict((square, digits) for square in squares)
    for square, digit in zip(squares, puzzle):
        if digit in digits and not place(grid, square, digit):
            return False  # Incongruent puzzle
    return grid


def place(grid, square, digit):
    """Eliminate all the other values (except digit) from
    grid[square] and propagate.
    Return grid, or False if a contradiction is detected.
    """
    other_vals = grid[square].replace(digit, '')
    if all(eliminate(grid, square, val) for val in other_vals):
        return grid
    return False


def eliminate(grid, square, digit):
    """Eliminate digit from grid[square]. Propagate when candidates
    are <= 2.
    Return grid, or False if a contradiction is detected.
    """
    if digit not in grid[square]:
        return grid  # already eliminated
    grid[square] = grid[square].replace(digit, '')

    ## (1) If a square is reduced to one value, eliminate value
    ## from peers.
    if len(grid[square]) == 0:
        return False  # nothing left to place here, wrong solution
    elif len(grid[square]) == 1:
        value = grid[square]
        if not all(
            eliminate(grid, peer, value) for peer in peers[square]
        ):
            return False

    ## (2) If a unit is reduced to only one place for a value,
    ## then put it there.
    for unit in units[square]:
        places = [sqr for sqr in unit if digit in grid[sqr]]
        if len(places) == 0:
            return False  # No place for this value
        elif len(places) == 1:
            # digit can only be in one place in unit,
            # assign it there
            if not place(grid, places[0], digit):
                return False
    return grid


def search(grid):
    if not grid:
        return False
    if all(len(grid[square]) == 1 for square in squares):
        return grid  # Solved
    values, square = min(
        (len(grid[square]), square) for square in squares
        if len(grid[square]) > 1
    )
    for digit in grid[square]:
        result = search(place(grid.copy(), square, digit))
        if result:
            return result


def solve(puzzle):
    grid = parse_puzzle(puzzle)
    return search(grid)


def measure(puzzle):
    start = time()
    res = solve(puzzle)
    return (res, time() - start)


def verify(res):
    def validate_unit(unit):
        return set(res[sqr] for sqr in unit) == set(digits)
    return res and all(validate_unit(unit) for unit in all_units)


def solve_batch(filename, stats=True):
    with open(filename) as stream:
        results, times = zip(*(
            measure(pzl.strip()) for pzl in stream.readlines()
        ))
    if stats:
        print_stats(len(results), times)

    if not all(verify(res) for res in results):
        print('Invalid results found!!!')

    return results


def display(grid):
    for row in chunk((grid[sqr] for sqr in squares), 9):
        print(''.join(row))
    print('-'*9)


def print_stats(n, times):
    tot_time = sum(times)
    mn, mx = min(times), max(times)
    avg, freq = tot_time/n, n/tot_time
    print(f'Solved {n} puzzles in {tot_time:.3f}s')
    print(f'Avg: {avg:.3f}s, Freq: {freq:.3f} puzzles/s')
    print(f'Min: {mn:.3f}s, Max: {mx:.3f}s')
    print()


if __name__ == '__main__':

    def test_structures():
        assert len(squares) == 81
        assert len(all_units) == 27
        assert all(len(units[square]) == 3 for square in squares)
        assert all(len(peers[square]) == 20 for square in squares)
        assert units['C3'] == [
            ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'],
            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
            ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'],
        ]
        assert peers['C3'] == set([
            'A3', 'B3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3',
            'C1', 'C2', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
            'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2',
        ])
        print('Structures tests passed.')

    PUZZLES_PATH = os.path.join('..', 'puzzles')

    def test_solver():
        puzzles = os.path.join(PUZZLES_PATH, 'sudoku-top95.txt')
        with open(puzzles) as stream:
            results = [solve(line.strip()) for line in stream]

            s = 0
            for res in results:
                s += int(res['A1'] + res['A2'] + res['A3'])
            if s == 49074:
                print('Solver is correct')
            else:
                print('Solver is incorrect')

    test_structures()
    test_solver()
    print()

    def solve_all():
        import os
        for entry in os.scandir(PUZZLES_PATH):
            if entry.name.startswith('sudoku-'):
                print(f'Solving {entry.name}')
                solve_batch(entry.path)

    solve_all()


"""
$ python solver.py
Structures tests passed.
Solver is correct

Solving sudoku-top95.txt
Solved 95 puzzles in 1.255s
Avg: 0.013s, Freq: 75.716 puzzles/s
Min: 0.003s, Max: 0.063s

Solving sudoku-top2365.txt
Solved 2365 puzzles in 19.187s
Avg: 0.008s, Freq: 123.262 puzzles/s
Min: 0.003s, Max: 0.084s

Solving sudoku-topn1465.txt
Solved 1465 puzzles in 17.951s
Avg: 0.012s, Freq: 81.613 puzzles/s
Min: 0.003s, Max: 0.241s

Solving sudoku-subig20.txt
Solved 17445 puzzles in 69.916s
Avg: 0.004s, Freq: 249.515 puzzles/s
Min: 0.003s, Max: 0.090s

Solving sudoku-topn234.txt
Solved 234 puzzles in 5.308s
Avg: 0.023s, Freq: 44.082 puzzles/s
Min: 0.003s, Max: 0.216s
"""
