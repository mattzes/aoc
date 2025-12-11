from aocd import get_data
from itertools import permutations

puzzle: str = get_data(day=9, year=2025)
# puzzle: str = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""

puzzle = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in puzzle.splitlines()]
pairs = list(permutations(puzzle, 2))

def get_next_pos(start, end):
    if start[0] > end[0]:
        return (start[0] - 1, start[1])
    elif start[0] < end[0]:
        return (start[0] + 1, start[1])
    elif start[1] > end[1]:
        return (start[0], start[1] - 1)
    elif start[1] < end[1]:
        return (start[0], start[1] + 1)

def get_line(start, end):
    line = [start]
    while start != end:
        start = get_next_pos(start, end)
        line.append(start)
    return line

outline = []
start = puzzle[-1]
for end in puzzle:
    line = get_line(start, end)
    outline.extend(line[1:])
    start = end

def is_point_in_polygon(p):
    n = len(puzzle)
    inside = False
    x, y = p

    for i in range(n):
        a = puzzle[i]
        b = puzzle[(i + 1) % n]
        
        # Check if point is in the outline
        if p in outline:
            return True
        
        # Ray casting algorithm
        xi, yi = a
        xj, yj = b
        if ((yi > y) != (yj > y)) and \
           (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi):
            inside = not inside
    return inside

ans = 0
for p1, p2 in pairs:
    cross1 = (p1[0], p2[1])
    cross2 = (p2[0], p1[1])
    if is_point_in_polygon(cross1) and is_point_in_polygon(cross2):
        result = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
        if result > ans:
            ans =result

print(f'Solution {ans}')