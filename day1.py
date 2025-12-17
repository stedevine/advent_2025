def solve(puzzle_input:str) -> int:
    # tokenize the input
    lines = puzzle_input.split("\n")
    
    # Imagine a safe dial with numbers from 0 -> 99
    # We want to count every time the dial is pointing at 0
    # It starts at 50, turn it to the left (L) decreases the value, 
    # right increases it.
    # We could implement some kind of circular buffer or maths that "when we go over 99 reset to 0 and when we go below 0 reset ot 99"
    # or we could increment the count everytime the result is exactly divisible by 100
    result = 0
    pointer = 50 
    for line in lines:
        delta = int(line[1:])
        if line[0] == 'L':
            pointer -= delta
        else:
            pointer += delta
    
        if pointer % 100 == 0:
            result += 1
        
    return result

def solve_two(puzzle_input:str, initial_position:int=50) -> int:
    lines = puzzle_input.split("\n")

    # Same as the above but increment everytime the dial 
    # passes through 0, it doesn't have to rest there.
    pointer = 50 
    result = 0

    for line in lines:
        delta = int(line[1:])
        
        # For every full turn (>100 clicks) we make, increment the number 
        # of times we pass though zero. 
        if delta > 100:
            result += int(delta/100)
            
            # Calculate the new delta (using the mod operator) - we can now ignore the complete turns
            # but we care about the number of remaining clicks
            delta = delta % 100

        assert delta < 100

        # Calculate the value of the pointer if we just applied increment or decrement.
        # This may push us out of range!
        if line[0] == "L":
            new_pointer = pointer - delta
        else:
            assert line[0] == "R"
            new_pointer = pointer + delta

        # Check if we're out of range - in that case we crossed 0!
        if (new_pointer < 0 or new_pointer > 99):            
            # The delta is less than 100 so if we started at 0, we didn't cross it
            if (pointer != 0):
                result += 1

        # Check if we're pointing at zero:
        if (new_pointer == 0):
            result += 1
            # Again, delta is less than 100, so we did not start at 0.
            assert (pointer != 0)


        # Update the pointer
        pointer = new_pointer
        # If we crossed zero, the value will be out of range - calculate the correct value
        if pointer < 0:
            pointer += 100

        if pointer > 99:
            pointer -= 100

        assert pointer >= 0
        assert pointer <= 99

    return result 

if __name__ == "__main__":
    with open('./day1_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        print(solve_two(puzzle_input))