with open('./2024/11/input.txt', 'r') as file:
    stones = file.read().split(" ")

BLINKS = 25

def blink(stones: list[str], blinks_left: int = BLINKS) -> int:
    print(blinks_left)
    count_stones = 0
    for stone in stones:
        if blinks_left == 0:
            count_stones += 1
            continue
        
        # rule number 1
        if stone == "0":
            count_stones += blink(["1"], blinks_left - 1)
            continue
        
        # rule number 2
        if len(stone) % 2 == 0:
            first_stone, second_stone = stone[:int(len(stone)/2)], stone[int(len(stone)/2):]
            second_stone = second_stone.lstrip("0")
            second_stone = second_stone if second_stone else "0"
            count_stones += blink([first_stone, second_stone], blinks_left - 1)
            continue
        new_stone = str(int(stone) * 2024)
        count_stones += blink([new_stone], blinks_left - 1)
    return count_stones
        

print(blink(stones))