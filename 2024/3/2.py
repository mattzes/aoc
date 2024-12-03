import re

with open('./2024/3/input.txt', 'r') as file:
    memory = file.read()

instruction_pattern = re.compile(r'do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)')
xy_pattern = re.compile(r'[0-9]{1,3}')

instructions = instruction_pattern.findall(memory)

result = 0
enable = True
for instruction in instructions:
    match instruction:
        case "do()":
            enable = True
        case "don't()":
            enable = False
        case _ if enable:
            x, y = map(int, xy_pattern.findall(instruction))
            result += x * y

print(result)