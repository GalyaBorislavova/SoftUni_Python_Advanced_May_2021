from collections import deque


chocolate = deque([int(el) for el in input().split(", ")])
cups_of_milk = deque([int(el) for el in input().split(", ")])

number_of_milkshakes = 0
success = False

while chocolate and cups_of_milk:
    current_chocolate = chocolate.pop()
    current_cup_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup_milk <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_milk)
        continue
    elif current_cup_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    if current_chocolate == current_cup_milk:
        number_of_milkshakes += 1

    else:
        cups_of_milk.append(current_cup_milk)
        current_chocolate -= 5
        chocolate.append(current_chocolate)

    if number_of_milkshakes == 5:
        success = True
        break


if success:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(el) for el in chocolate])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(el) for el in cups_of_milk])}")
else:
    print("Milk: empty")