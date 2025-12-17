def solve(puzzle_input:str) -> int:
    result = 0
    for battery in puzzle_input.split('\n'):
        result += get_max_joltage(battery)
    
    return result


def solve_two(puzzle_input:str) -> int:
    return 0

def get_max_joltage(battery:str) -> int:
    # Get the position of the largest value
    battery_values = [int(i) for i in battery]
    largest_value = max(battery_values)
    position = battery_values.index(largest_value)

    # Special case - largest number is at the end of the sequence
    if (position == len(battery_values)-1):
        next_largest_value = max(battery_values[0:-1])
        return (next_largest_value * 10) + largest_value

    next_largest_value = max(battery_values[position+1:])
    position = battery_values.index(largest_value)
    return (largest_value * 10) + next_largest_value

if __name__ == "__main__":
    with open('./day3_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        #print(solve_two(puzzle_input))