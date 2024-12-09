with open('./2024/6/input.txt', 'r') as file:
    map = [list(line) for line in file.read().split('\n')]

def get_starting_point() -> tuple:
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^':
                return (x, y)
    return None



def count_steps():
    possible_obs = 0
    starting_position = get_starting_point()

    for Y in range(len(map)):
        for X in range(len(map[0])):
            directions = [
                (0, -1), # up
                (1, 0), # right
                (0, 1), # down
                (-1, 0), # left
            ]
            x, y = starting_position
            path = set()
            
            if (X, Y) == starting_position:
                continue
            
            while True:
                if (x, y, directions[0]) in path:
                    possible_obs += 1
                    break

                path.add((x, y, directions[0]))
                dx, dy = directions[0]
                x_in_front = x + dx
                y_in_front = y + dy
                
                
                if not (0 <= y_in_front < len(map) and 0 <= x_in_front < len(map[0])):
                    break
                
                if map[y_in_front][x_in_front] == '#' or (x_in_front, y_in_front) == (X, Y):
                    directions.append(directions.pop(0))
                else:
                    x = x_in_front
                    y = y_in_front


    return possible_obs

print(count_steps())