from collections import deque


def print_data(created_bombs, bomb_effects, bomb_casings):
    if bomb_effects:
        print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
    else:
        print(f"Bomb Effects: empty")
    if bomb_casings:
        print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")
    else:
        print(f"Bomb Casings: empty")

    for bomb_type, count in sorted((created_bombs.items()), key=lambda x: x[0]):
        print(f"{bomb_type} Bombs: {count}")

    exit(0)


effects = deque([int(el) for el in input().split(", ")])
casings = [int(el) for el in input().split(", ")]

bombs = {
    "Datura": 0,
    "Cherry": 0,
    "Smoke Decoy": 0
}
success = False

while effects and casings:
    current_effect = effects.popleft()
    current_casing = casings.pop()

    current_sum = current_effect + current_casing

    if current_sum == 40:
        bombs["Datura"] += 1
    elif current_sum == 60:
        bombs["Cherry"] += 1
    elif current_sum == 120:
        bombs["Smoke Decoy"] += 1
    else:
        current_casing -= 5
        if current_casing >= 0:
            casings.append(current_casing)
        effects.appendleft(current_effect)

    for value in bombs.values():
        if not value >= 3:
            success = False
            break
        success = True
    if success:
        print("Bene! You have successfully filled the bomb pouch!")
        print_data(bombs, effects, casings)
        break

if not success:
    print("You don't have enough materials to fill the bomb pouch.")
    print_data(bombs, effects, casings)
