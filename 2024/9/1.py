with open('./2024/9/input.txt', 'r') as file:
    disk_map = list(file.read())

# calculate the length of each block and mark them with block index
turing_tape = []
for i, val in enumerate(disk_map):
    if i % 2 == 0: # files
        for j in range(int(val)):
            turing_tape.append(int(i/2))
    else: # space
        for j in range(int(val)):
            turing_tape.append(".")

# sort dots to the end
left_index = 0
right_index = len(turing_tape) - 1
while left_index < right_index:
    
    while turing_tape[left_index] != ".":
        left_index += 1
    
    while turing_tape[right_index] == ".":
        right_index -= 1
    
    # swap
    turing_tape[left_index], turing_tape[right_index] = turing_tape[right_index], turing_tape[left_index]
    # move to next, avoid swap back
    left_index += 1
    right_index -= 1

# sum up the checksum
checksum = 0
for index, block_number in enumerate(turing_tape):
    if block_number == ".":
        break
    checksum += index * int(block_number)

print(checksum)

