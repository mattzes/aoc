with open('./2024/5/input.txt', 'r') as file:
    input = file.read().split('\n')

split_index = input.index('')
updates = [update.split(",") for update in input[split_index + 1:]]

allowed_right = {}
allowed_left = {}
for x, y in (order.split("|") for order in input[:split_index]):
    allowed_right.setdefault(x, []).append(y)
    allowed_left.setdefault(y, []).append(x)

def is_order_valid_to_left(page, left_pages) -> bool:
    if page in allowed_right.keys():
        for left_page in left_pages:
            if left_page in allowed_right[page]:
                # print("left") # issue is on the right site
                return False
    return True

def is_order_valid_to_right(page, right_pages) -> bool:
    if page in allowed_left.keys():
        for right_page in right_pages:
            if right_page in allowed_left[page]:  
                # print("right") # issue is on the left site
                return False
    return True

def is_update_invalid(update) -> tuple:
    for i, page in enumerate(update):
        left_pages = update[:i]
        right_pages = update[i + 1:]
        if not is_order_valid_to_left(page, left_pages):
            return i, "left"
        if not is_order_valid_to_right(page, right_pages):
            return i, "right"
    return False, ""

def get_new_index(update, index_of_reordering_page, direction) -> int:
    if direction == "right":
        index = 0
        for page in update[index_of_reordering_page + 1:]:
            if page in allowed_left[update[index_of_reordering_page]]:
                index = update.index(page)
        return index
    if direction == "left":
        index = len(update)
        for page in update[:index_of_reordering_page]:
            if page in allowed_right[update[index_of_reordering_page]]:
                index = update.index(page)
        return index

def order_pages(update: list, index_of_reordering_page: int, direction: str) -> list:
    ordered_pages = update.copy()
    new_index = get_new_index(update, index_of_reordering_page, direction)
    page_to_reorder = ordered_pages.pop(index_of_reordering_page)
    ordered_pages.insert(new_index, page_to_reorder)
    return ordered_pages

def cehck_updates():
    page_sum = 0
    for update in updates:
        reordered_update = update.copy()
        invalid, direction = is_update_invalid(update)
        while type(invalid) == int:
            reordered_update = order_pages(reordered_update, invalid, direction)
            invalid, direction = is_update_invalid(reordered_update)
            if type(invalid) == bool:
                page_sum += int(reordered_update[len(reordered_update) // 2])
            
    
    return page_sum

print(cehck_updates())
        