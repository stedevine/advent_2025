import pytest
from day2 import solve, solve_two, does_sequence_repeat_n_times, has_multiple_repeating_values

def tests() -> None:
    puzzle_input =  """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    assert(1227775554 == solve(puzzle_input))
    assert(4174379265 == solve_two(puzzle_input))
    
@pytest.mark.large
def test_full_input():
    with open('./day2_input') as f:
        puzzle_input = f.read()
        assert(18952700150 == solve(puzzle_input))
        assert(28858486244 == solve_two(puzzle_input))


def test_sequence_repeat():
    assert does_sequence_repeat_n_times("11",1)
    assert does_sequence_repeat_n_times("1212",1)
    assert does_sequence_repeat_n_times("1111",1)
    assert does_sequence_repeat_n_times("100100",1)

    assert not does_sequence_repeat_n_times("12",1)
    assert not does_sequence_repeat_n_times("121",1)
    assert not does_sequence_repeat_n_times("100101",1)

    assert does_sequence_repeat_n_times("111",2)
    assert does_sequence_repeat_n_times("121212",2)
    assert does_sequence_repeat_n_times("123123123",2)

    assert not does_sequence_repeat_n_times("101",2)
    assert not does_sequence_repeat_n_times("12121",2)

    assert does_sequence_repeat_n_times("12121212",3)
    assert does_sequence_repeat_n_times("1212121212",4)

def test_has_multiple_repeating_values():
    # Invalid codes
    assert has_multiple_repeating_values(22)
    assert has_multiple_repeating_values(333)
    assert has_multiple_repeating_values(4444)
    assert has_multiple_repeating_values(1212)
    assert has_multiple_repeating_values(121212)
    assert has_multiple_repeating_values(123123)
    assert has_multiple_repeating_values(12341234)
    assert has_multiple_repeating_values(12121212)
    assert has_multiple_repeating_values(123123123)
    assert has_multiple_repeating_values(1212121212)
    assert has_multiple_repeating_values(1234512345)
    assert has_multiple_repeating_values(1212121212)

    # Valid codes
    assert not has_multiple_repeating_values(1)
    assert not has_multiple_repeating_values(123)
    assert not has_multiple_repeating_values(1234)
    assert not has_multiple_repeating_values(12345)
    assert not has_multiple_repeating_values(123456)
    assert not has_multiple_repeating_values(1234567)
    assert not has_multiple_repeating_values(12345678)
    assert not has_multiple_repeating_values(123456789)
    assert not has_multiple_repeating_values(1234567890)
    
