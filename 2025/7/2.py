from aocd import get_data

puzzle: str = get_data(day=7, year=2025)
# puzzle: str = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

puzzle: list[str] = puzzle.splitlines()
beams = {
    puzzle.pop(0).index("S"): 1
}

ans = 0
for line in puzzle:
    
    # a little optimization
    if '^' not in line:
        continue
    
    
    new_beams = {}
    for beam, n in beams.items():
        if line[beam] == '^':
            new_beams[beam + 1] = new_beams.get(beam + 1, 0) + n
            new_beams[beam - 1] = new_beams.get(beam - 1, 0) + n
        else:
            new_beams[beam] = new_beams.get(beam, 0) + n

    beams = new_beams


print(f'Solution: {sum(beams.values())}')