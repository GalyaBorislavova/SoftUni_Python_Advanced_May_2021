from collections import deque

END_COMMAND = "End"
START_COMMAND = "Start"

people = deque()

quantity = int(input())

while True:
    name = input()
    if name == START_COMMAND:
        break
    else:
        people.append(name)

while True:
    command = input()
    if command == END_COMMAND:
        break
    elif command.startswith("refill"):
        command = command.split()
        litters_to_add = int(command[1])
        quantity += litters_to_add
    elif command.isdigit():
        current_person = people.popleft()
        needed_litters = int(command)
        if needed_litters <= quantity:
            quantity -= needed_litters
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait")

print(f"{quantity} liters left")