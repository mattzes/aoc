from aocd import get_data

puzzle: str = get_data(day=11, year=2025)
# puzzle: str = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""

routes = {}
for line in puzzle.splitlines():
    key, value = line.split(":")
    routes[key] = value.split()

ans = 0
stack = routes['you']
while stack:
    key = stack.pop(-1)
    values = routes[key]
    for value in values:
        if value == "out":
            ans += 1
        else:
            stack.append(value)
    

print(f'Solution {ans}')