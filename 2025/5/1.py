from aocd import get_data

puzzle: str = get_data(day=5, year=2025)
# puzzle = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""

puzzle = puzzle.split("\n\n")
id_ranges = puzzle[0].splitlines()
ids = puzzle[1].splitlines()

id_ranges = [(int(start), int(end)) for start, end in (id_range.split("-") for id_range in id_ranges)]

ans = 0
for id in ids:
    for start, end in id_ranges:
        if start <= int(id) <= end:
            ans += 1
            break

print(f'Solution: {ans}')