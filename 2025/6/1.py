from aocd import get_data
import math

puzzle: str = get_data(day=6, year=2025)
# puzzle: str = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

# separate numbers of math problemns into lists
problems = []
for line in puzzle.splitlines():
    problems.append(line.split())

ans = 0
for i in range(len(problems[0])):
    numbers = []
    for row in problems[:-1]:
        numbers.append(int(row[i]))

    if problems[-1][i] == "+":
        ans += sum(numbers)
    else:
        ans += math.prod(numbers)



print(f'Solution: {ans}')