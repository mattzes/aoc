with open('./2024/4/input.txt', 'r') as file:
    word_search = []
    
    # Iterate through each line
    for line in file:
        # Split the line inot a list of letters
        word_search.append(list(line.strip()))

Y_RANGE = len(word_search)
X_RANGE = len(word_search[0])
DIRECTIONS = [
    (0, 1), # to right
    (1, 1), # to lower right
    (1, 0), # to lower
    (1, -1), # to lower left
    (0, -1), # to left
    (-1, -1), # to upper left
    (-1, 0), # to upper
    (-1, 1) # to upper right
]
WORD_TO_FIND = 'XMAS'

def count_xmas_directions(y, x):
    count = 0
    for direction in DIRECTIONS:
        for i in range(1, len(WORD_TO_FIND)):
            new_x = x + direction[1] * i
            new_y = y + direction[0] * i
            if new_y < 0 or new_y >= Y_RANGE or new_x < 0 or new_x >= X_RANGE:
                # break, because we are out of bounds
                break
            if word_search[new_y][new_x] != WORD_TO_FIND[i]:
                # break, because the letter is not the one we are looking for
                break
            if i == 3:
                count += 1
    return count

def count_xmas():
    count = 0
    for y in range(len(word_search)):
        for x in range(len(word_search[y])):
            if word_search[y][x] == WORD_TO_FIND[0]:
                count += count_xmas_directions(y, x)
                
    return count

print(count_xmas())
