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

for y, line in enumerate(puzzle_lines):
    for x, element in enumerate(line):
        if element == "@":
            count_ajacent_rolls = 0
            for dy, dx in ADJACENT_OFFSETS:
                adjacent_y, adjacent_x = y+dy, x+dx
                if (0 <= adjacent_y < GRID_HEIGHT) and (0 <= adjacent_x < GRID_WIDTH) and puzzle_lines[adjacent_y][adjacent_x] == "@":
                    count_ajacent_rolls += 1
            if count_ajacent_rolls < 4:
                ans += 1

print(f'Solution: {ans}')