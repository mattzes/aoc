with open('./2024/10/input.txt', 'r') as file:
    topo = [[int(stone) if stone != "." else -1 for stone in stones] for stones in file.read().split('\n')]

ROW = len(topo)
COL = len(topo[0])

directions = [
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
    (-1, 0) # up
]

def count_posible_paths(pos: tuple[int, int], prev_val: int = 0) -> int:
    path_count = set()
    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        # Check if new position is out of bounds
        if not (0 <= new_pos[0] < ROW and 0 <= new_pos[1] < COL):
            continue
        
        # check if new position is a possible next step or a end point
        new_val = topo[new_pos[0]][new_pos[1]]
        if new_val == prev_val + 1:
            if new_val == 9:
                path_count.add(new_pos)
            else:
                path_count.update(count_posible_paths(new_pos, new_val))
    return path_count


path_count = 0
for row in range(ROW):
    for col in range(COL):
        if topo[row][col] == 0:
            path_count += len(count_posible_paths((row, col)))

print(path_count)