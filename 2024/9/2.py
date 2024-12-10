with open('./2024/9/input.txt', 'r') as file:
    disk_map = list(file.read())

# calculate the length of each block and mark them with block index
turing_tape: list[list[str]]= []
for i, val in enumerate(disk_map):
    if val == "0":
        continue
    blocks = []
    turing_tape.append([])
    for j in range(int(val)):
        if i % 2 == 0: # files
            turing_tape[-1].append(str(int(i/2)))
        else: # space
            turing_tape[-1].append(".")

# sort files into spaces
left_index = 0
left_border = 0
right_border = len(turing_tape) - 1

for right_index in range(right_border, -1, -1):
    if "." in turing_tape[right_index] or len(set(turing_tape[right_index])) != 1:
        continue
    
    for left_index in range(right_index):
        if turing_tape[left_index].count(".") >= len(turing_tape[right_index]):
            blocks_to_move = turing_tape[right_index].copy()
            # replacing the first spaces which are found in the left blocks with the right file blocks
            turing_tape[left_index] = [blocks_to_move.pop(0) if char == "." and blocks_to_move else char for char in turing_tape[left_index]]
            turing_tape[right_index] = ["." for _ in range(len(turing_tape[right_index]))]
            break

# sum up the checksum
checksum = 0
index = -1
for blocks in turing_tape:
    for block in blocks:
        index += 1
        if block == ".":
            continue
        checksum += index * int(block)

print(checksum)

