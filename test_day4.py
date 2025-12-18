import pytest
from day4 import solve, solve_two

def tests() -> None:
    puzzle_input =  """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""   
    assert 13 == solve(puzzle_input)
    assert 43  == solve_two(puzzle_input)

@pytest.mark.large
def test_full_input():
    with open('./day4_input') as f:
        puzzle_input = f.read()
        assert(1602 == solve(puzzle_input))
        assert(9518 == solve_two(puzzle_input))