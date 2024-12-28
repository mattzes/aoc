import re

with open('./2024/13/input.txt', 'r') as file:
    raw_machines = file.read().split('\n\n')


machine_pattern = r"[-+]?\d+"

machines = [
    {
        'A': [int(n) for n in re.findall(machine_pattern, block.splitlines()[0])],
        'B': [int(n) for n in re.findall(machine_pattern, block.splitlines()[1])],
        'Prize': [int(n) + 10000000000000 for n in re.findall(machine_pattern, block.splitlines()[2])],
    }
    for block in raw_machines
]

sum_of_prices = 0
for machine in machines:
    A0, A1 = machine['A']
    B0, B1 = machine['B']
    P0, P1 = machine['Prize']
    
    D = A0 * B1 - A1 * B0
    Dx = P0 * B1 - P1 * B0
    Dy = A0 * P1 - A1 * P0

    if D == 0:
        continue

    A = Dx / D
    B = Dy / D

    if not (A.is_integer() and B.is_integer()):
        continue

    A, B = int(A), int(B)
    sum_of_prices += A * 3 + B * 1

print(sum_of_prices)