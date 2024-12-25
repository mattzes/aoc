import re

with open('./2024/13/input.txt', 'r') as file:
    raw_machines = file.read().split('\n\n')


machine_pattern = r"[-+]?\d+"

machines = [
    {
        'A': [int(n) for n in re.findall(machine_pattern, block.splitlines()[0])],
        'B': [int(n) for n in re.findall(machine_pattern, block.splitlines()[1])],
        'Prize': [int(n) for n in re.findall(machine_pattern, block.splitlines()[2])],
    }
    for block in raw_machines
]

sum_of_prices = 0
for machine in machines:
    x_max = max(machine['Prize'][0] // machine['A'][0], machine['Prize'][1] // machine['A'][1])
    if x_max > 100:
        x_max = 100
    
    
    best_price = 0
    for x in range(x_max):
        poss_y = (machine['Prize'][0] - x * machine['A'][0]) // machine['B'][0]
        
        if poss_y > 100:
            continue
        
        verify = bool(poss_y * machine['B'][1] + x * machine['A'][1] == machine['Prize'][1])
        if verify:
            price = x * 3 + poss_y * 1
            if price > best_price:
                best_price = price
    sum_of_prices += best_price

print(sum_of_prices)