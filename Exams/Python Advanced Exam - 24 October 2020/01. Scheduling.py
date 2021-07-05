from collections import deque

tasks = deque([int(el) for el in input().split(", ")])
searched_index = int(input())

complete = sorted([(el, ind) for ind, el in enumerate(tasks)])
cycles = 0

while complete:
    for el in complete:
        if el[1] == searched_index:
            cycles += el[0]
            print(cycles)
            exit(0)
        else:
            cycles += el[0]