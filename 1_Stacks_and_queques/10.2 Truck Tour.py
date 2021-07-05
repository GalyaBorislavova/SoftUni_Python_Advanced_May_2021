from collections import deque

number_of_stations = int(input())
stations = deque([])

for s in range(number_of_stations):
    stations.append([el for el in input().split()])

for big_circle in range(number_of_stations):
    is_valid = True
    tank_fuel = 0
    for small_circle in range(number_of_stations):
        tank_fuel += int(stations[small_circle][0]) - int(stations[small_circle][1])
        if tank_fuel < 0:
            stations.append(stations.popleft())
            is_valid = False
            break
    if is_valid:
        print(big_circle)
        break
