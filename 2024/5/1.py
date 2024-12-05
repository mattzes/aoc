with open('./2024/5/input.txt', 'r') as file:
    input = file.read().split('\n')

split_index = input.index('')
updates = [update.split(",") for update in input[split_index + 1:]]

orders_x = {}
orders_y = {}
for x, y in (order.split("|") for order in input[:split_index]):
    orders_x.setdefault(x, []).append(y)
    orders_y.setdefault(y, []).append(x)

def check_order(page, left_pages, right_pages) -> bool:
    if page in orders_x.keys() and any(left_page in orders_x[page] for left_page in left_pages):
        return False
    if page in orders_y.keys() and any(right_page in orders_y[page] for right_page in right_pages):
        return False
    return True

def is_update_valid(update) -> bool:
    for i, page in enumerate(update):
        left_pages = update[:i]
        right_pages = update[i + 1:]
        if not check_order(page, left_pages, right_pages):
            return False
    return True

def cehck_updates():
    page_sum = 0
    for update in updates:
        if is_update_valid(update):
            page_sum += int(update[len(update) // 2])
    
    return page_sum

print(cehck_updates())
        