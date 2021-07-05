from collections import deque

kids = deque(input().split())
step = int(input())

while len(kids) > 1:
    kids.rotate(step)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")