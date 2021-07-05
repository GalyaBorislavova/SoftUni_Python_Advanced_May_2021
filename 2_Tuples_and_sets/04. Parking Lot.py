def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


n = int(input())
data = input_to_list(n)

parking_lot = set()

for car in data:
    command, number = car.split(", ")
    if command == "IN":
        parking_lot.add(number)
    else:
        parking_lot.remove(number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")