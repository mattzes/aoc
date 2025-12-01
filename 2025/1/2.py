from aocd import get_data

puzzle: str = get_data(day=1, year=2025)


pointer = 50
counter = 0

for comb in puzzle.splitlines():
    direction = comb[:1]
    steps = int(comb[1:])
    
    if direction == "R":
        pointer = pointer + steps
        counter += int(pointer / 100)
        pointer = pointer % 100
    elif direction == "L":
        if pointer == 0:
            counter -= 1
        pointer = pointer - steps
        if pointer <= 0:
            counter += int(pointer / -100) + 1
        pointer = pointer % 100

print(counter)