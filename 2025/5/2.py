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
id_ranges = [(int(start), int(end)) for start, end in (id_range.split("-") for id_range in puzzle[0].splitlines())]
id_ranges.sort()

merged_ranges = []
current_start, current_end = id_ranges[0]

for start, end in id_ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start = start
        current_end = end
merged_ranges.append((current_start, current_end))


ans = sum(end - start + 1 for start, end in merged_ranges)

print(f'Solution: {ans}')