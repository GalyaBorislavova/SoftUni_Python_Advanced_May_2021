from collections import deque

cup_capacity = deque([int(el) for el in input().split()])
bottles_with_water = [int(el) for el in input().split()]

wastedLitters_of_water = 0
no_filled_yet = False

while True:
    if cup_capacity and not no_filled_yet:
        current_cup_capacity = cup_capacity.popleft()
    if bottles_with_water:
        current_litters_water = bottles_with_water.pop()
    if current_litters_water >= current_cup_capacity:
        wastedLitters_of_water += current_litters_water - current_cup_capacity
    current_cup_capacity -= current_litters_water
    if current_cup_capacity <= 0:
        no_filled_yet = False
    else:
        if not bottles_with_water:
            no_filled_yet = False
        else:
            no_filled_yet = True
    if (len(cup_capacity) == 0 or len(bottles_with_water) == 0) and not no_filled_yet:
        break

if cup_capacity:
    result = []
    print("Cups:", end=" ")
    while cup_capacity:
        result.append(str(cup_capacity.popleft()))
    print(f"{' '.join(result)}")
    print(f"Wasted litters of water: {wastedLitters_of_water}")

elif bottles_with_water:
    result = []
    print("Bottles:", end=" ")
    while bottles_with_water:
        result.append(str(bottles_with_water.pop()))
    print(f"{' '.join(result)}")
    print(f"Wasted litters of water: {wastedLitters_of_water}")

