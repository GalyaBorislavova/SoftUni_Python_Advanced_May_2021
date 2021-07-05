data = input()

stack = []

for i in range(len(data)):
    char = data[i]
    if char == "(":
        stack.append(i)
    elif char == ")":
        start = stack.pop()
        print(data[start:i + 1])
