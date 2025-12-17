from typing import Callable

def solve(puzzle_input:str) -> int:
    # part 1 - the input is invalid if the code sequence is repeated exactly once
    return sub_solve(puzzle_input, has_single_repeating_sequence)

def solve_two(puzzle_input:str) -> int:
    # part 2 - the input is invalud if the code sequence repeats one or more times
    return sub_solve(puzzle_input, has_multiple_repeating_values)

def has_single_repeating_sequence(code:int) -> bool:
    return does_sequence_repeat_n_times(str(code),1)

def does_sequence_repeat_n_times(code_str:str, repeats:int) -> bool:
    assert repeats > 0
    assert repeats < 6

    if (len(code_str) % (repeats + 1)) == 0:
        block_size = int(len(code_str)/(repeats + 1))
        block = code_str[0:block_size]

        for i in range(1, repeats + 1):
            start = (i*block_size)
            end = start + block_size 
            if block != code_str[start:end]:
                return False
        return True
    
    return False

def has_multiple_repeating_values(code:int) -> bool:
    code_str = str(code)
    # Special case : all the digits are the same
    if (len(code_str) > 1):
        if (len(set(list(code_str)))) == 1:
            return True

    # By analyzing the input, we know the lengths of the product codes 
    # range between 1 and 10.
    # For each length, consider how we might see repeating blocks

    if len(code_str) == 4:
        # One possible repeat: xyxy
        return does_sequence_repeat_n_times(code_str, 1)

    if len(code_str) == 6:
        # Two possible repeats: xyzxyz xyxyxy
        return (does_sequence_repeat_n_times(code_str, 1) or does_sequence_repeat_n_times(code_str, 2))

    if len(code_str) == 8:
        # Two possible repeats: wxyzwxyz xyxyxyxy
        return (does_sequence_repeat_n_times(code_str, 1) or does_sequence_repeat_n_times(code_str, 3))

    if len(code_str) == 9:
        # One possible repeat: xyzxyzxyz
        return (does_sequence_repeat_n_times(code_str, 2))

    if len(code_str) == 10:
        # Two possible repeats: vwxyzvwxyz xyxyxyxyxy
        return (does_sequence_repeat_n_times(code_str, 1) or does_sequence_repeat_n_times(code_str, 4))

    return False

# Iterate over the input, extract the codes
# Use the passed in function to determine if the code is valid
def sub_solve(puzzle_input: str, is_code_invalid:Callable[[int],bool]) ->int:
    # tokenize the input
    product_codes = puzzle_input.split(",")

    result = 0
    for product_code in product_codes:
        start = product_code.split('-')[0]
        end = product_code.split('-')[1]
    
        for i in range(int(start), int(end)+1):
            if is_code_invalid(i):
                result += i
    return result

if __name__ == "__main__":
    with open('./day2_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        print(solve_two(puzzle_input))