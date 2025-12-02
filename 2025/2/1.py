from aocd import get_data

# puzzle = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
puzzle = get_data(day=2, year=2025)
ans = 0

for id_range in puzzle.split(","):
    start, end = map(int, id_range.split("-"))

    for id in range(start, end + 1):
        id = str(id)
        
        if len(id) % 2 == 0:
            first_half = id[int(len(id) / 2):]
            second_half = id[:int(len(id) / 2)]
            
            if first_half == second_half:
                ans += int(id)

print(f'Solution: {ans}')