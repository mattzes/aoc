from aocd import get_data

puzzle: str = get_data(day=4, year=2025)
# puzzle: str = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

# define some constants
ADJACENT_OFFSETS = [
    (-1, -1),  # top-left
    (-1,  0),  # top
    (-1,  1),  # top-right
    ( 0, -1),  # left
    ( 0,  1),  # right
    ( 1, -1),  # bottom-left
    ( 1,  0),  # bottom
    ( 1,  1)   # bottom-right
]
puzzle_lines = puzzle.splitlines()
GRID_HEIGHT = len(puzzle_lines)
GRID_WIDTH = len(puzzle_lines[0])

ans = 0
prev_ans = None

def remove_rolls(grid: list[str]):
    count_removed_rolls = 0
    for y, line in enumerate(grid):
        for x, element in enumerate(line):
            if element == "@":
                
                # count rolls in the 8 adjacent positions
                count_ajacent_rolls = 0
                for dy, dx in ADJACENT_OFFSETS:
                    adjacent_y, adjacent_x = y+dy, x+dx
                    if (0 <= adjacent_y < GRID_HEIGHT) and (0 <= adjacent_x < GRID_WIDTH) and puzzle_lines[adjacent_y][adjacent_x] == "@":
                        count_ajacent_rolls += 1
                
                # remove a roll and count them if they have less than 4 rolls in the 8 adjacent positons
                if count_ajacent_rolls < 4:
                    grid[y] = grid[y][:x] + "x" + grid[y][x+1:]
                    count_removed_rolls += 1

    return grid, count_removed_rolls

# remove rolls as long as rolls can be remved
while prev_ans != ans:
    prev_ans = ans
    puzzle_lines, count_removed_rolls = remove_rolls(puzzle_lines)
    ans += count_removed_rolls

print(f'Solution: {ans}')