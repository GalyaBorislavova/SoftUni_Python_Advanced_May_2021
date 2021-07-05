clothes = [int(el) for el in input().split()]
capacity_of_rack = int(input())

number_of_racks = 1

current_rack = capacity_of_rack
while clothes:
    current_volume = clothes.pop()
    if current_volume <= current_rack:
        current_rack -= current_volume
    else:
        number_of_racks += 1
        current_rack = capacity_of_rack
        current_rack -= current_volume

print(number_of_racks)