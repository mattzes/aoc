from itertools import product

with open('./2024/7/input.txt', 'r') as file:
    equations = file.read().split('\n')

combinations_store = {1: [('+'), ('*')]}

def get_operator_combinations(length: int) -> list:
    if length in combinations_store :
        return combinations_store[1]
    else:
        operator = ['+', '*']
        operator_combinations = []
        for combination in product(operator, repeat=length):
            operator_combinations.append(combination)
        return operator_combinations


def evaluate(result: int, calibrations: list) -> bool:
    operator_combinations = get_operator_combinations(len(calibrations) - 1)
    for combination in operator_combinations:
        new_result = calibrations[0]
        for i in range(1, len(calibrations)):
            if combination[i - 1] == '+':
                new_result += calibrations[i]
            else:
                new_result *= calibrations[i]
        if new_result == result:
            return True
    return False
        

def sum_up_correct_equations() -> int:
    equations_sum = 0
    for equation in equations:
        result, calibrations = equation.split(': ')
        calibrations = [int(num) for num in calibrations.split(' ')]
        if evaluate(int(result), calibrations):
            equations_sum += int(result)
    return equations_sum

print(sum_up_correct_equations())