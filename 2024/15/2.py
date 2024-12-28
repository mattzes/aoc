from collections import deque

with open('./2024/15/input.txt', 'r') as file:
    input = file.read().split('\n\n')
    warehouse = [list(line) for line in input[0].split('\n')]
    moves = list(input[1].replace('\n', ''))


def get_direction(move):
    match move:
        case '^': return -1, 0
        case 'v': return 1, 0
        case '<': return 0, -1
        case '>': return 0, 1

# finding the starting position
for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col] == '@':
            start= (row, col)
            break

# moving the robot
for move in moves:
    direction = get_direction(move)
    
    stack = deque([start])
    while stack:
        current_position = stack[-1]
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        
        if warehouse[next_position[0]][next_position[1]] == 'O':
            stack.append(next_position)
            continue
        
        if warehouse[next_position[0]][next_position[1]] == '.':
            if warehouse[current_position[0]][current_position[1]] == '@':
                start = next_position
            warehouse[next_position[0]][next_position[1]] = warehouse[current_position[0]][current_position[1]]
            warehouse[current_position[0]][current_position[1]] = '.'
            stack.pop()
            continue
        
        if warehouse[next_position[0]][next_position[1]] == '#':
            break

# sum up the gps coordinates of all the objects
sum_gps = 0
for r, row in enumerate(warehouse):
    for c, cell in enumerate(row):
        if cell == 'O':
            sum_gps += 100 * r + c
print(sum_gps)