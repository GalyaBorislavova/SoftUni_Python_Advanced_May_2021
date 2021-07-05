from collections import deque

quantity = int(input())
orders = deque(int(i) for i in input().split())

max_order = max(orders)
print(max_order)

while orders:
    current_order = orders.popleft()
    if current_order <= quantity:
        quantity -= current_order
    else:
        orders.appendleft(current_order)
        break

if orders:
    print(f"Orders left:", ' '.join([str(e) for e in orders]))
else:
    print("Orders complete")
