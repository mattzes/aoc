with open('./2024/6/input.txt', 'r') as file:
    map = [list(line) for line in file.read().split('\n')]

def get_starting_point() -> tuple:
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^':
                return (x, y)
    return None

directions = [
    (0, -1), # up
    (1, 0), # right
    (0, 1), # down
    (-1, 0), # left
]

def count_steps():
    steps = 1
    position = get_starting_point()
    map[position[1]][position[0]] = 'X'
    
    while True:
        x, y = position
        dx, dy = directions[0]
        position = (x + dx, y + dy)
        
        if not (0 <= position[1] < len(map)) or not (0 <= position[0] < len(map[position[1]])):
            break
        elif map[position[1]][position[0]] == '#':
            position = (x, y)
            directions.append(directions.pop(0))
        elif map[position[1]][position[0]] != 'X':
            map[position[1]][position[0]] = 'X'
            steps += 1
    return steps

print(count_steps())