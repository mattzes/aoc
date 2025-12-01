from collections import deque

with open('./2024/15/test2-input.txt', 'r') as file:
    input = file.read().split('\n\n')
    warehouse = [list(line) for line in input[0].split('\n')]
    moves = list(input[1].replace('\n', ''))

def get_direction(move):
    match move:
        case '^': return -1, 0
        case 'v': return 1, 0
        case '<': return 0, -1
        case '>': return 0, 1

# finding the starting position and building a warehouse two times wider
for r, row in enumerate(warehouse):
    new_row = []
    for c, cell in enumerate(row):
        match cell:
            case '@':
                start = (r, c * 2)
                new_row.append(cell)
                new_row.append('.')
            case 'O':
                new_row.append('[')
                new_row.append(']')
            case '.' | '#':
                new_row.append(cell)
                new_row.append(cell)
    warehouse[r] = new_row


# moving the robot
for move in moves:
    direction = get_direction(move)
    
    stack = deque([start])
    while stack:
        

# sum up the gps coordinates of all the objects
sum_gps = 0
for r, row in enumerate(warehouse):
    for c, cell in enumerate(row):
        if cell == '[':
            sum_gps += 100 * r + c
print(sum_gps)