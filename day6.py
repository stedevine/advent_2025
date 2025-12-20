from typing import Tuple
import math 
def solve(puzzle_input:str) -> int:
    result = 0
    rows = get_rows(puzzle_input)
    # The operators are on the bottom row
    number_input = rows[0:-1]
    operators = rows[-1]

    for col in range(0, len(rows[0])):
        multiply, column_result = get_operation_and_initial_result(operators[col])

        for n in number_input:
            if multiply:
                column_result *= int(n[col])
            else:
                column_result += int(n[col])
        result += column_result

    return result

def get_rows(puzzle_input:str) -> list[str]:
    rows = []
    for input_row in puzzle_input.split("\n"):
        # Split on space, remove any empty items
        rows.append(list(filter(lambda t: len(t) > 0, input_row.split(" "))))

    # Confirm all the rows have the same number of items
    number_of_problems = len(rows[0])
    assert all(len(r) == number_of_problems for r in rows)

    return rows


def solve_two(puzzle_input:str) -> int:
    result = 0

    print(puzzle_input)
    rows =  puzzle_input.split("\n")

    
    #assert len(rows) == 4

    operators = rows[len(rows)-1]
    left_index = 0
    right_index = 0
    pointer = 1        

    running = True
    while running:

        while pointer < len(operators) and operators[pointer] == ' ':
            pointer += 1

        
        right_index = pointer
        print(f"left {left_index} right {right_index} pointer {pointer}")

        numbers = get_numbers(left_index, right_index, rows)
        if len(numbers) == 0:
            running = False
            break

        #print(numbers)
        #print(operators[left_index])
        #print(get_result(numbers, operators[left_index]))
        result += get_result(numbers, operators[left_index])
        left_index = right_index
        right_index = left_index 
        pointer = left_index + 1
        

    print()

    
    

    print(operators)
    
    return result

def get_result(numbers:list[int], op:str):
    if op == "*":
        return math.prod(numbers)

    assert op == "+"
    return sum(numbers)



def get_numbers(left_index:int, right_index:int, rows:list[str]) -> list[int]:
    numbers: list[int] = []

    for index in range(left_index, right_index):
        col = 0
        num = []
        for col in range(len(rows)-1):
            if index < len(rows[col]) and rows[col][index] != " ":
                num.append(rows[col][index])
                print(num)
        if (len(num)> 0):
            numbers.append(int(''.join(num)))
    
    return numbers


def get_operation_and_initial_result(operator:str) -> Tuple[bool, int]:
    if operator == "*":
        return (True, 1)
        multiply = True
        result = 1
    else:
        assert operator == "+"
        return (False, 0)

if __name__ == "__main__":
    with open('./day6_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        print(solve_two(puzzle_input))
