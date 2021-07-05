data = input()

stack = []

for char in data:
    stack.append(char)

result = ""

while stack:
    result += stack.pop()

print(result)