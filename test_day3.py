import pytest
from day3 import solve, solve_two, get_max_joltage

def tests() -> None:
    puzzle_input =  """987654321111111
811111111111119
234234234234278
818181911112111"""   
    assert 357 == solve(puzzle_input)

@pytest.mark.parametrize(
    "battery, expected",
    [
        pytest.param("987654321111111", 98),
        pytest.param("811111111111119", 89),
        pytest.param("234234234234278", 78),
        pytest.param("818181911112111", 92),
    ],
)

def test_get_joltage_2(battery:str, expected:int) -> None:
    assert expected == get_max_joltage(battery,2)

@pytest.mark.parametrize(
    "battery, expected",
    [
        pytest.param("987654321111111", 987654321111),
        pytest.param("811111111111119", 811111111119),
        pytest.param("234234234234278", 434234234278),
        pytest.param("818181911112111", 888911112111),
    ],
)

def test_get_joltage_12(battery:str, expected:int) -> None:
    assert expected == get_max_joltage(battery,12)

def test_full_input():
    with open('./day3_input') as f:
        puzzle_input = f.read()
        assert(17408 == solve(puzzle_input))
        assert(172740584266849 == solve_two(puzzle_input))