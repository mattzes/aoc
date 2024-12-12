with open('./2024/11/input.txt', 'r') as file:
    stones = file.read().split(" ")

BLINKS = 75
cache = {}

def blink(stone: str, blinks_left: int = BLINKS) -> int:
    if (stone, blinks_left) in cache:
        return cache[(stone, blinks_left)]    
    
    count_stones = 0
    if blinks_left == 0:
        count_stones += 1
    
    # rule number 1
    elif stone == "0":
        count_stones += blink("1", blinks_left - 1)
    
    # rule number 2
    elif len(stone) % 2 == 0:
        first_stone, second_stone = stone[:int(len(stone)/2)], stone[int(len(stone)/2):]
        second_stone = second_stone.lstrip("0")
        second_stone = second_stone if second_stone else "0"
        count_stones += blink(first_stone, blinks_left - 1)
        count_stones += blink(second_stone, blinks_left - 1)
    else:
        new_stone = str(int(stone) * 2024)
        count_stones += blink(new_stone, blinks_left - 1)
    
    cache[(stone, blinks_left)] = count_stones
    
    return count_stones
        
stone_count = 0
for stone in stones:
    stone_count += blink(stone)
print(stone_count)