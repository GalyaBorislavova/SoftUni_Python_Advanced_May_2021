names = input().split(", ")

heroes = {name: {"items": [], "cost": 0} for name in names}

command = input().split("-")
while not command[0] == "End":
    name, item, cost = command
    cost = int(cost)
    if name in heroes:
        if item not in heroes[name]["items"]:
            heroes[name]["items"].append(item)
            heroes[name]["cost"] += cost
    command = input().split("-")

for name, dict_data in heroes.items():
    print(f"{name} -> Items: {len(heroes[name]['items'])}, Cost: {heroes[name]['cost']}")