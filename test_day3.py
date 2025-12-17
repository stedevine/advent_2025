import pytest
from day3 import solve, get_max_joltage

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

def test_get_joltage(battery:str, expected:int) -> None:
    assert expected == get_max_joltage(battery)
