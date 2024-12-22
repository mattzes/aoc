with open('./2024/12/input.txt', 'r') as file:
    garden_input = [list(line) for line in file.read().splitlines()]


class Garden:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
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

    def calc_perimeter(self, cluster) -> int:
        perimeter = 0
        for flower in cluster:
            for direction in self.directions:
                new_pos = (flower[0] + direction[0], flower[1] + direction[1])
                if new_pos not in cluster:
                    perimeter += 1
        return perimeter

    def get_price(self, cluster) -> int:
        perimeter = self.calc_perimeter(cluster)
        return perimeter * len(cluster)

    def sum_prices(self) -> int:
        return sum([self.get_price(cluster) for cluster in self.flower_clusters])

garden = Garden(garden_input)
garden.check_garden()
print(garden.sum_prices())