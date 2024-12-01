with open('./2024/1/input.txt', 'r') as file:
    left_list = []
    right_list = []
    
    # Iterate through each line
    for line in file:
        # Split the line by whitespace
        left, right = line.split()
        # Append to respective lists
        left_list.append(int(left))
        right_list.append(int(right))

counts = {}
result = 0

for i, n in enumerate(left_list):
    if n in counts.keys():
        result += counts[n]
    else:
        count = right_list.count(n) * n
        counts[n] = count
        result += count

print(result)
