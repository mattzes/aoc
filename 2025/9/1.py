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
pairs = permutations(puzzle, 2)

ans = 0
for p1, p2 in pairs:
    result = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    if result > ans:
        ans =result

print(f'Solution {ans}')