from collections import deque

n = int(input())
stations = deque([])

for _ in range(n):
    line = input().split()
    fuel, distance = int(line[0]), int(line[1])
    stations.append([fuel, distance])

for i in range(n):
    fuel_tank = 0
    travelled = 0
    for pump in stations:
        fuel, distance = pump[0], pump[1]
        fuel_tank += fuel
        if fuel_tank < distance:
            break
        else:
            fuel_tank -= distance
            travelled += 1
    if travelled == len(stations):
        print(i)
        break
    stations.rotate(-1)