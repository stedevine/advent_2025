from day6 import solve, solve_two

def tests() -> None:
    puzzle_input =  """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """   
    assert 4277556 == solve(puzzle_input)
    assert 3263827  == solve_two(puzzle_input)

def test_full_input():
    with open('./day6_input') as f:
        puzzle_input = f.read()
        assert(3261038365331 == solve(puzzle_input))
        assert(8342588849093 == solve_two(puzzle_input))