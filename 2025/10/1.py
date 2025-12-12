from aocd import get_data
from itertools import combinations

puzzle: str = get_data(day=10, year=2025)
# puzzle: str = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


maschines = []
for maschine in puzzle.splitlines():
    lights_len = 0
    lights_target = []
    buttons = []
    for device in maschine.split():
        if "[" in device:
            lights_len = len(device) - 2
            lights_target = int(device[1:-1].replace(".", "0").replace("#", "1"), 2)
        if "(" in device:
            positions = [int(x) for x in device.strip("()").split(",")]
            bits = [0] * lights_len
            for pos in positions:
                bits[pos] = 1
            buttons.append(int("".join(map(str, bits)), 2))
    maschines.append((lights_target, buttons))

ans = 0
for lights, buttons in maschines:
    buttons_combs = []
    for r in range(1, len(buttons)):
        buttons_combs.extend(combinations(buttons, r))

    for buttons_comb in buttons_combs:
        current_lights = 0
        for button in buttons_comb:
            current_lights = current_lights ^ button
        if current_lights == lights:
            ans += len(buttons_comb)
            break


print(f'Solution {ans}')