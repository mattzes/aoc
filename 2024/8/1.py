from itertools import combinations

with open('./2024/8/input.txt', 'r') as file:
    city = [list(road) for road in file.read().split('\n')]

ROW = len(city)
COL = len(city[0])

def get_tower_positions() -> dict[str, list[tuple[int, int]]]:
    tower_positions = {}
    for row in range(ROW):
        for col in range(COL):
            if city[row][col] != '.':
                tower_positions.setdefault(city[row][col], []).append((row, col))
    return tower_positions

def build_tower_pairs(tower_positions: dict[str, list[tuple[int, int]]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    tower_pairs = {}
    for tower_id, positions in tower_positions.items():
        if len(positions) == 1:
            tower_pairs.setdefault(tower_id, []).extend(positions)
        else:
            tower_pairs.setdefault(tower_id, []).extend(list(combinations(positions,2)))
    return tower_pairs

def calculate_distances(tower_pairs: dict[str, list[tuple[tuple[int, int], tuple[int, int]]]]) -> dict[str, list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]]:
    tower_pairs_with_distances = {}
    for tower_id, pairs in tower_pairs.items():
        for pair in pairs:
            row = pair[0][0] - pair[1][0]
            col = pair[0][1] - pair[1][1]
            tower_pairs_with_distances.setdefault(tower_id, []).append((*pair, (row, col)))
    return tower_pairs_with_distances

def calculate_antinodes(tower_pairs_with_distances: dict[str, list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]]) -> set[tuple[int, int]]:
    antinodes = set()
    for pairs in tower_pairs_with_distances.values():
        for pair in pairs:
            pos1 = pair[0]
            pos2 = pair[1]
            
            distance = pair[2]
            negative_distance = (-distance[0], -distance[1])
            
            antinode1 = (pos1[0] + distance[0], pos1[1] + distance[1])
            antinode2 = (pos2[0] + negative_distance[0], pos2[1] + negative_distance[1])
            
            if 0 <= antinode1[0] < ROW and 0 <= antinode1[1] < COL:
                antinodes.add(antinode1)
            if 0 <= antinode2[0] < ROW and 0 <= antinode2[1] < COL:
                antinodes.add(antinode2)
    return antinodes
    

tower_pairs = build_tower_pairs(get_tower_positions())
tower_pairs_with_distances = calculate_distances(tower_pairs)

calculated_antinodes = calculate_antinodes(tower_pairs_with_distances)
print(len(calculated_antinodes))