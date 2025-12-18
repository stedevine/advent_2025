def solve(puzzle_input:str) -> int:
    grid = Grid(puzzle_input)
    return grid.count_adjacent()

def solve_two(puzzle_input:str) -> int:
    grid = Grid(puzzle_input)
    total_removed = 0
    while True:
        removed = grid.remove_rolls()
        if removed == 0:
            break
        total_removed += removed
    return total_removed


class Grid:
    def __init__(self, text:str):
        text_rows = text.split('\n')
        self.width = len(text_rows[0])
        self.height = len(text_rows)
        self.rows : list[list[str]]= [list(r) for r in text_rows]

    def count_adjacent(self) -> int:
        result = 0
        for r in range(0, self.height):
            for c in range(0, self.width):  
                if self.is_removable((c,r)):
                    result += 1 

        return result            

    def remove_rolls(self) -> int:
        removable_rolls = []
        for r in range(0, self.height):
            for c in range(0, self.width):  
                if self.is_removable((c,r)):
                    removable_rolls.append((c,r))

        for removable_roll in removable_rolls:
            c,r = removable_roll
            self.rows[r][c] = '.'

        return len(removable_rolls)


    def is_removable(self, point:tuple[int,int]) -> bool:
        c,r = point

        if self.get_value((c,r)) != "@":
            # Nothing to remove
            return False
        
        assert self.get_value((c,r)) == "@"

        # These are the adjecent points:
        nw = (c-1,r-1)
        nn = (c, r-1)
        ne = (c+1, r-1)

        ww = (c-1, r)
        ee = (c+1, r)

        sw = (c-1, r+1)                              
        ss = (c, r+1)                              
        se = (c+1, r+1)

        adjacent = [
            self.get_value(nw),
            self.get_value(nn),
            self.get_value(ne),

            self.get_value(ww),
            self.get_value(ee),

            self.get_value(sw),
            self.get_value(ss),
            self.get_value(se)
            ]
        return adjacent.count("@") < 4

    # Get the value at the point. It will be a dot(.) an at (@)
    # or an empty string if the point is out of bounds
    def get_value(self, point:tuple[int,int]) -> str:
        c, r = point
        result = " "
        if c < 0 or c > self.width-1:
            result = " "
        elif r < 0 or r > self.height-1:
            result = " "
        else:
            result = self.rows[r][c]
        return result                     

    def print(self) -> None:
        for r in range(0, self.height):
            print_row:list[str] = []
            for c in range(0, self.width):
                print_row.append(self.rows[r][c])
            print(''.join(print_row))


if __name__ == "__main__":
    with open('./day4_input') as f:
        puzzle_input = f.read()
        print(solve(puzzle_input))
        print(solve_two(puzzle_input))
