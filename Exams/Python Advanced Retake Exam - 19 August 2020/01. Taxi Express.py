from collections import deque

customers = deque([int(c) for c in input().split(", ")])
taxis = [int(t) for t in input().split(", ")]

total_time = 0
while customers:
    current_customer = customers.popleft()
    if taxis:
        current_taxi = taxis.pop()
        if current_taxi >= current_customer:
            total_time += current_customer

        else:
            customers.appendleft(current_customer)
            continue
    else:
        customers.appendleft(current_customer)
        break


if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")