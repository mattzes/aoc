left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]
result = 0

left_list.sort()
right_list.sort()

for l, r in zip(left_list, right_list):
    if l > r:
        result += (l - r)
    else:
        result += (r - l)

print(result)