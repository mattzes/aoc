# import lines as matrix
with open ('./2024/2/input.txt', 'r') as file:
    reports = []
    
    for line in file:
        reports.append([int(number) for number in line.split()])

count_safe_reports = 0

def is_report_safe(report: list) -> bool:
    # to keep track of fluctuating over the report, indicates the first fluctuation
    level_difference = report[1] - report[0]
    if level_difference > 0:
        current_trend = "increasing"
    elif level_difference < 0:
        current_trend = "decreasing"
    else:
        return False # Unsafe, first two numers are equal
    
    for i in range(len(report) - 1):
        level_difference = report[i + 1] - report[i]
        
        if  (current_trend == "increasing" and level_difference not in [1, 2, 3]) or \
            (current_trend == "decreasing" and level_difference not in [-1, -2, -3]):
                return False
    return True

for report in reports:
    if is_report_safe(report):
        count_safe_reports += 1

print(f'{count_safe_reports} of {len(reports)} are safe reports')