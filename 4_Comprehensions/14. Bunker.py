import re

categories = input().split(", ")
n = int(input())

bunker = {cat: {"items": [], "quality": 0, "quantity": 0} for cat in categories}

pattern = r"[0-9]+"
for _ in range(n):
    element_data = input()
    category, item_name, quality_quantity_data_list = element_data.split(" - ")
    result = re.findall(pattern, quality_quantity_data_list)
    quantity, quality = [int(el) for el in result]
    if item_name not in bunker[category]["items"]:
        bunker[category]["items"].append(item_name)
        bunker[category]["quality"] += quality
        bunker[category]["quantity"] += quantity

print(f"Count of items: {sum([bunker[cat]['quantity'] for cat in bunker])}")
print(f"Average quality: {(sum([bunker[cat]['quality'] for cat in bunker]) / len(categories)):.2f}")
for key in bunker:
    print(f"""{key} -> {', '.join(bunker[key]["items"])}""")
