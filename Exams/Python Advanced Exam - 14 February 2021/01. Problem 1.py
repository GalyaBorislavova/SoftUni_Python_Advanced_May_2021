from collections import deque


def print_show_in_both_cases(effects_list, power_list, palm, willow, crossette):
    if effects_list:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")

    if power_list:
        print(f" Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

    print(f"Palm Fireworks: {palm}")
    print(f"Willow Fireworks: {willow}")
    print(f"Crossette Fireworks: {crossette}")


def valid_input(number):
    return number > 0


def needed_number_of_every_type_fireworks(palm, willow, crossette):
    return palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3
firework_effects = deque(list(filter(valid_input, [int(num) for num in input().split(", ")])))
explosive_power = deque(list(filter(valid_input, [int(num) for num in input().split(", ")])))

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:

    if needed_number_of_every_type_fireworks(palm_firework, willow_firework, crossette_firework):
        break

    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()

    current_sum = current_power + current_effect

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        palm_firework += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        willow_firework += 1
    elif current_sum % 5 == 0 and current_sum % 3 == 0:
        crossette_firework += 1
    else:
        current_effect -= 1
        if valid_input(current_effect):
            firework_effects.append(current_effect)
        explosive_power.append(current_power)


if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
    print_show_in_both_cases(firework_effects, explosive_power, palm_firework, willow_firework,
                             crossette_firework)
else:
    print("Sorry. You can't make the perfect firework show.")
    print_show_in_both_cases(firework_effects, explosive_power, palm_firework, willow_firework,
                             crossette_firework)


