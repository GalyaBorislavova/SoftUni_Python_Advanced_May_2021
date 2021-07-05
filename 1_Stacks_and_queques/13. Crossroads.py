from collections import deque

END_COMMAND = "END"
green_light_duration = int(input())
free_window_duration = int(input())

cars = deque([])
everyone_is_safe = True
number_of_cars = 0

car = input()
while not car == END_COMMAND:
    if not everyone_is_safe:
        break
    if car == "green":
        if cars:
            current_car = cars.popleft()
            left_seconds_green_light = green_light_duration - len(current_car)
            while left_seconds_green_light > 0:
                number_of_cars += 1
                if cars:
                    current_car = cars.popleft()
                    left_seconds_green_light -= len(current_car)
                else:
                    break
            if left_seconds_green_light == 0:
                number_of_cars += 1
            if free_window_duration >= abs(left_seconds_green_light):
                if left_seconds_green_light < 0:
                    number_of_cars += 1
            else:
                hit_car = current_car
                hit_character = current_car[free_window_duration + left_seconds_green_light]
                print("A crash happened!")
                print(f"{hit_car} was hit at {hit_character}.")
                everyone_is_safe = False
                break
    else:
        cars.append(car)
    car = input()

if everyone_is_safe:
    print("Everyone is safe.")
    print(f"{number_of_cars} total cars passed the crossroads.")
