from aocd import get_data
from math import sqrt
from itertools import permutations

puzzle: str = get_data(day=8, year=2025)
# puzzle: str = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""

junction_boxes: list = [tuple(map(int, line.split(','))) for line in puzzle.splitlines()]

distances = {}
for start_junction_box, end_junction_box in permutations(junction_boxes, 2):
    distances[(start_junction_box, end_junction_box)] = sqrt(sum([(start_junction_box[i]-end_junction_box[i])**2 for i in range(3)]))

distances = dict(
    sorted(distances.items(), key=lambda item: item[1])
)

circuits: list[list] = [[junction_box] for junction_box in junction_boxes]
while len(circuits) > 1:
    start, end = next(iter(distances))
    
    # merge circuits
    start_circuit = []
    end_circuit = []
    for circuit in circuits:
        if start in circuit:
            start_circuit = circuit
        if end in circuit:
            end_circuit = circuit
        if start_circuit and end_circuit:
            break
    if start_circuit is not end_circuit:
        circuits.append(start_circuit + end_circuit)
        circuits.remove(start_circuit)
        circuits.remove(end_circuit)
    
    distances.pop((start, end))
    distances.pop((end, start))


print(f'Solution: {start[0] * end[0]}')