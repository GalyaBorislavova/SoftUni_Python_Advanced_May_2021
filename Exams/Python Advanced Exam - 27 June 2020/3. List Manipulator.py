from collections import deque


def list_manipulator(numbers, command, end_type, *args):
    numbers = deque(numbers)

    if command == "add":
        if end_type == "beginning":
            for num in reversed(args):
                numbers.appendleft(num)
        elif end_type == "end":
            for num in args:
                numbers.append(num)
    elif command == "remove":
        if end_type == "beginning":
            if args:
                for r in range(args[0]):
                    if numbers:
                        numbers.popleft()
            else:
                if numbers:
                    numbers.popleft()
        elif end_type == "end":
            if args:
                for r in range(args[0]):
                    if numbers:
                        numbers.pop()
            else:
                if numbers:
                    numbers.pop()

    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
