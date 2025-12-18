def solve(puzzle_input:str) -> int:
    result = 0
    for battery in puzzle_input.split('\n'):
        result += get_max_joltage(battery,2)
    return result


def solve_two(puzzle_input:str) -> int:
    result = 0
    for battery in puzzle_input.split('\n'):
        result += get_max_joltage(battery,12)
    return result

def get_max_joltage(battery:str, cell_size:int) -> int:
    # Similar to the simple implementation, but we must use eaxctly 12 cells the battery

    # Need to make sure we'll always have enough cells remaining to populate 
    # the result.
    # Use a variable size window to pick the largest available value
    index = 0
    max_battery: list[str] = []
    window_size = len(battery) - cell_size + 1 

    while len(max_battery) < cell_size:
        
        window = battery[index:index+window_size]
        max_value_in_window = max(window)
        position = window.index(max_value_in_window)
        # If the position of the max value in the window is not at 0
        # we'll need to shrink the window
        window_size = window_size - position
        index = index + 1 + position

        max_battery.append(max_value_in_window)

    return int(''.join(max_battery))

if __name__ == "__main__":
    with open('./day3_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        print(solve_two(puzzle_input))

"""
# Specific, simple implementation for two cells
def get_max_joltage(battery:str) -> int:
    # For a given sequence of numbers pick the two 
    # that, when combined give the largest value.
    # The sequence order may not be changed

    # Generally we'll want to return the largest
    # value in the sequence followed by the next largest
    # Unless the largest is at the end of the sequence, 
    # in which case we want to return the next largest followed
    # by the largest

    # Get the position of the largest value
    battery_values = battery
    largest_value = max(battery_values)
    position = battery_values.index(largest_value)

    if (position == len(battery_values)-1):
        # largest value is at the end of the sequence
        next_largest_value = max(battery_values[0:-1])
        return int(next_largest_value) * 10 + int(largest_value)

    next_largest_value = max(battery_values[position+1:])
    position = battery_values.index(largest_value)
    return int(largest_value) * 10 + int(next_largest_value)
"""
