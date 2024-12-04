with open('./2024/4/input.txt', 'r') as file:
    word_search = []
    
    # Iterate through each line
    for line in file:
        # Split the line inot a list of letters
        word_search.append(list(line.strip()))

Y_RANGE = len(word_search)
X_RANGE = len(word_search[0])

def is_a_cross(y: int, x: int) -> bool:
    is_a_cross = 0
    for dy, dx in [(-1, -1), (-1, 1)]:
        upper_y, upper_x = y + dy, x + dx
        lower_y, lower_x = y - dy, x - dx
        if (word_search[upper_y][upper_x], word_search[lower_y][lower_x]) in {("M", "S"), ("S", "M")}:
            is_a_cross += 1
    return is_a_cross == 2

def count_xmas():
    count = 0
    for y in range(1, len(word_search) - 1):
        for x in range(1, len(word_search[y]) - 1):
            if word_search[y][x] == "A" and is_a_cross(y, x):
                count += 1

    return count

print(count_xmas())
