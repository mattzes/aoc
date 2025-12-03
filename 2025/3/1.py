from aocd import get_data

puzzle: str = get_data(day=3, year=2025)

# puzzle = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

ans = 0

for bank in puzzle.splitlines():
    l = list(bank)
    
    first = max(l[:-1])
    first_pos = l.index(first)
    last = max(l[first_pos + 1:])
    ans += int(f'{first}{last}')

print(f'Solution: {ans}')