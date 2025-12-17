from day1 import solve, solve_two

def tests() -> None:
    puzzle_input =  """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    assert(3 == solve(puzzle_input))
    assert(6 == solve_two(puzzle_input))
    assert(10 == solve_two("R1000"))
    assert(1 == solve_two("L51"))
    assert(1 == solve_two("R51"))
    assert(1 == solve_two("L50"))
    assert(1 == solve_two("R50"))
    

def test_full_input():
    with open('./day1_input') as f:
        puzzle_input = f.read()
        assert(1129 == solve(puzzle_input))
        assert(6638 == solve_two(puzzle_input))
