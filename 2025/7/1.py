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
BORDER = len(puzzle[0])
beams = set([puzzle.pop(0).index("S")])

ans = 0
for line in puzzle:
    new_beams = set()
    for beam in beams:
        if line[beam] == '^':
            ans += 1
            if beam + 1 < BORDER:
                new_beams.add(beam + 1)
            if 0 <= beam - 1:
                new_beams.add(beam - 1)
        else:
            new_beams.add(beam)
    beams = new_beams
    
    # only for visualization
    for beam in beams:
        line = line[:beam] + '|' + line[beam+1:]
    print(line)

print(f'Solution: {ans}')