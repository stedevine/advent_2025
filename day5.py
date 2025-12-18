import bisect 
from typing import Tuple

def get_ranges_items(puzzle_input:str) -> Tuple[list[Tuple[int, int]], list[int]]:
    ranges = []
    items = []
    populate_ranges = True
    for line in puzzle_input.split("\n"):
        if line == "":
            populate_ranges = False
            continue
        if populate_ranges:
            ranges.append(line)
        else:
            items.append(int(line))

    int_ranges = [ ((int(r.split('-')[0])), (int(r.split('-')[1]))) for r in ranges]
    return(int_ranges, items)

def solve(puzzle_input:str) -> int:
    ranges, items = get_ranges_items(puzzle_input)
    start_ranges = sorted(ranges, key=lambda r:r[0])
    end_ranges = sorted(ranges, key=lambda r:r[1])

    fresh = []
    for item in items:
        if item < start_ranges[0][0]:
            # item is smaller than the lowest value in the bottom range
            continue
        
        if item > end_ranges[-1][1]:
            # item is larger than the highest value in the top range
            continue

        # find the closest start ranage that is than or equal to the item
        start_range_index = bisect.bisect_left(start_ranges, item, key=lambda r:r[0])
        start_range = start_ranges[start_range_index-1]
        # find the closest end range that is greater than or equal to the item
        end_range_index = bisect.bisect_right(end_ranges, item, key=lambda r:r[1])
        end_range = end_ranges[end_range_index]
        #print(f"item {item} {start_range} /  {end_range}")

        if item >= start_range[0] and item <= start_range[1]:
            fresh.append(item)
        elif item <= end_range[1] and item >= end_range[0]:
            fresh.append(item)
        
    return len(fresh)

def solve_two(puzzle_input:str) -> int:
    ranges, items = get_ranges_items(puzzle_input)
    start_ranges = sorted(ranges, key=lambda r:r[0])

    # keep track of the highest value added to the index
    highest = 0
    total = 0

    for r in start_ranges:
        if r[0] > highest:
            total += r[1]+1 - r[0]
            highest = r[1]
        elif r[1] > highest:
            total += r[1] - highest
            highest = r[1]
    
    return total


if __name__ == "__main__":
    with open('./day5_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        print(solve_two(puzzle_input))
