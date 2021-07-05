from collections import deque

price_per_bullet = int(input())
size_barrel = int(input())
bullets = [int(el) for el in input().split(" ")]
locks = deque([int(el) for el in input().split(" ")])
value_of_intelligence = int(input())

number_of_bullets = 0
empty = False

while locks:
    current_lock = locks.popleft()
    if bullets:
        current_bullet = bullets.pop()
        number_of_bullets += 1
    else:
        locks.appendleft(current_lock)
        break
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    if number_of_bullets % size_barrel == 0 and bullets:
        print("Reloading!")
else:
    empty = True
if empty:
    bullet_cost = number_of_bullets * price_per_bullet
    money_earned = value_of_intelligence - bullet_cost
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")