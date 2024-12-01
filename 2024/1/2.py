left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]

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
