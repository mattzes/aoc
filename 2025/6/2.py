from aocd import get_data
import math

puzzle: str = get_data(day=6, year=2025)
# puzzle: str = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

# separate numbers of math problemns into lists
# also get the lengs of ech column
problems = puzzle.splitlines()
operator_line = problems.pop()
operator = operator_line.split()
num_lens = operator_line.replace('*', '+').split('+')[1:]
problems = list(map(list, problems))

ans = 0
for i, operator in enumerate(operator):
    col_numbers = []
    for _ in range(len(num_lens[i]) + 1):
        num = []
        for line in problems:
            num.append(line.pop(0))
        num = ''.join(num)
        if not num.isspace():
            col_numbers.append(int(''.join(num)))

    if operator == "+":
        ans += sum(col_numbers)
    else:
        ans += math.prod(col_numbers)


print(f'Solution: {ans}')