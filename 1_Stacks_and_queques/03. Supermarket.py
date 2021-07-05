from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

people = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{len(people)} people remaining.")
        break
    elif command == PAID_COMMAND:
        while people:
            print(people.popleft())
    else:
        people.append(command)