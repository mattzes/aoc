from aocd import get_data

# puzzle = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
puzzle = get_data(day=2, year=2025)
ans = 0

def id_is_valid(id: str) -> bool:
    chunk_lengths = [i for i in range(1, len(id) + 1) if (len(id)) % i == 0]
    for chunk_lenght in chunk_lengths:
        chunks = [id[i:i+chunk_lenght] for i in range(0, len(id), chunk_lenght)]
        if len(chunks) >= 2:
            chunks = set(chunks)
            if len(chunks) == 1:
                return True
    return False

for id_range in puzzle.split(","):
    start, end = map(int, id_range.split("-"))

    for id in range(start, end + 1):
        id = str(id)
        
        if id_is_valid(id):
            ans += int(id)

print(f'Solution: {ans}')