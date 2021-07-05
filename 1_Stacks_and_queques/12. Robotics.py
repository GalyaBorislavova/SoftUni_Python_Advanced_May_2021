from collections import deque
from datetime import datetime, timedelta

END_COMMAND = "End"
products = deque([])
robots = []
available_robots = deque([])

robots_data = input().split(";")
start_time = datetime.strptime(input(), "%H:%M:%S")

for el in robots_data:
    current_robot = el.split("-")
    robot = {"name": current_robot[0], "processing_time": int(current_robot[1]), "available_at": start_time}
    robots.append(robot)
    available_robots.append(robot)

product = input()
while not product == END_COMMAND:
    products.append(product)
    product = input()

time = start_time + timedelta(seconds=1)
while len(products) > 0:
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r["available_at"]:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)