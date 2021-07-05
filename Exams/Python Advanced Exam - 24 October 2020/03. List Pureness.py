from collections import deque


def best_list_pureness(numbers: deque, k: int):
    numbers = deque(numbers)
    pureness = {}

    for rotation in range(k + 1):
        current_pureness = sum([num * ind for ind, num in enumerate(numbers)])
        pureness[rotation] = current_pureness

        numbers.rotate()

    for rotation, pureness in sorted(pureness.items(), key=lambda x: -x[1]):
        return f"Best pureness {pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
