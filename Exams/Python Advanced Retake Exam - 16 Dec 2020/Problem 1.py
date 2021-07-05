from collections import deque


def valid_input(number: int):
    return number > 0


def special_case(number):
    return number % 25 == 0


males = list(filter(valid_input, [int(el) for el in input().split()]))
females = deque(list(filter(valid_input, [int(el) for el in input().split()])))

number_of_matches = 0

while males and females:
    current_male = males.pop()
    if special_case(current_male):
        if males:
            males.pop()
        continue

    current_female = females.popleft()

    if special_case(current_female):
        if females:
            females.popleft()
            males.append(current_male)
        continue

    if current_female == current_male:
        number_of_matches += 1
    else:
        current_male -= 2
        if valid_input(current_male):
            males.append(current_male)

print(f"Matches: {number_of_matches}")

if males:
    print(f"Males left: {', '.join([str(el) for el in reversed(males)])}")

else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")
