from day5 import solve, solve_two

def tests() -> None:
    puzzle_input =  """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""   
    assert 3 == solve(puzzle_input)
    assert 14  == solve_two(puzzle_input)

def test_overlapping_ranges() -> None:
    puzzle_input =  """3-5
5-6
10-12
14-16
15-22
15-17
100-101

1
"""
    assert 18 == solve_two(puzzle_input)

def test_full_input():
    with open('./day5_input') as f:
        puzzle_input = f.read()
        assert(758 == solve(puzzle_input))
        assert(343143696885053 == solve_two(puzzle_input))

