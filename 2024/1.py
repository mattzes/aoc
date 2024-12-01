with open('./2024/input.txt', 'r') as file:
    left_list = []
    right_list = []
    
    # Iterate through each line
    for line in file:
        # Split the line by whitespace
        left, right = line.split()
        # Append to respective lists
        left_list.append(int(left))
        right_list.append(int(right))

result = 0

left_list.sort()
right_list.sort()

for l, r in zip(left_list, right_list):
    if l > r:
        result += (l - r)
    else:
        result += (r - l)

print(result)