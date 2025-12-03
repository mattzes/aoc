from aocd import get_data

puzzle: str = get_data(day=3, year=2025)

# puzzle = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

ans = 0

for bank in puzzle.splitlines():
    l = list(bank)
    
    batteries = []
    for i in range(12):
        first = max(l[:len(l)-11+i])
        batteries.append(first)
        l = l[l.index(first)+1:]

    ans += int("".join(batteries))

print(f'Solution: {ans}')