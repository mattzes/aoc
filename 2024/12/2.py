with open('./2024/12/input.txt', 'r') as file:
    garden_input = [list(line) for line in file.read().splitlines()]


class Garden:
    directions = [
        (0, 1), # right
        (1, 0), # down
        (0, -1), # left
        (-1, 0) # up
    ]
    
    def __init__(self, garden):
        self.garden = garden
        self.already_in_cluster = set()
        self.flower_clusters = []


    def get_unique_flower_cluster(self, searchable_flower, pos):
        cluster = set()
        if pos in self.already_in_cluster:
            return cluster
        else:
            if self.garden[pos[0]][pos[1]] == searchable_flower:
                if pos not in self.already_in_cluster:
                    cluster.add(pos)
                    self.already_in_cluster.add(pos)

                    for direction in self.directions:
                        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                        if new_pos[0] < 0 or new_pos[0] >= len(self.garden) or new_pos[1] < 0 or new_pos[1] >= len(self.garden[0]):
                            continue
                        else:
                            cluster.update(self.get_unique_flower_cluster(searchable_flower, new_pos))

        return cluster


    def check_garden(self):
        for row in range(len(self.garden)):
            for col in range(len(self.garden[row])):
                cluster = self.get_unique_flower_cluster(self.garden[row][col], (row, col))
                if cluster:
                    self.flower_clusters.append(cluster)

    def get_fence_posistions(self, cluster) -> set:
        fence_positions = set()
        for flower in cluster:
            for direction in self.directions:
                new_pos = (flower[0] + direction[0], flower[1] + direction[1])
                if new_pos not in cluster:
                    fence_positions.add(new_pos)
        return fence_positions
    
    def get_one_side(self, fence_positions, pos, direction_one, direction_two) -> tuple:
        side = set()
        side.add(pos)
        for direction in [direction_one, direction_two]:
            current_pos = pos
            while True:
                new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                if new_pos in fence_positions:
                    side.add(new_pos)
                    current_pos = new_pos
                else:
                    break
        side = list(side)
        side.sort()
        return tuple(side)
    
    def count_sides(self, cluster, fence_positions) -> int:
        sides = set()
        for flower in cluster:
            for i, direction in enumerate(self.directions):
                new_pos = (flower[0] + direction[0], flower[1] + direction[1])
                if new_pos in fence_positions:
                    sides.add((direction, self.get_one_side(fence_positions, new_pos, self.directions[i - 1], self.directions[(i + 1) % 4])))
        return len(sides)

    def get_price(self, cluster) -> int:
        sides = self.count_sides(cluster, self.get_fence_posistions(cluster))
        
        result = sides * len(cluster)
        pos = next(iter(cluster))
        print(f'{self.garden[pos[0]][pos[1]]},{len(cluster)},{sides},{result}')
        return result

    def sum_prices(self) -> int:
        return sum([self.get_price(cluster) for cluster in self.flower_clusters])

garden = Garden(garden_input)
garden.check_garden()
print(garden.sum_prices())