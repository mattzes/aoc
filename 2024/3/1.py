import re

with open('./2024/3/input.txt', 'r') as file:
    memory = file.read()

mul_pattern = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')
xy_pattern = re.compile(r'[0-9]{1,3}')

muls = mul_pattern.findall(memory)

result = 0
for mul in muls:
    x, y = map(int, xy_pattern.findall(mul))
    print
    result += x * y

print(result)

