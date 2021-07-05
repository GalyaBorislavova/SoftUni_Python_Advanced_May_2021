import sys

n = int(input())

sequence = []

for query in range(n):
    current_query = input()
    if current_query.startswith("1"):
        current_query = current_query.split()
        element_to_add = int(current_query[1])
        sequence.append(element_to_add)
    elif current_query == "2":
        if sequence:
            del sequence[-1]
    elif current_query == "3":
        if sequence:
            print(max(sequence))
    elif current_query == "4":
        if sequence:
            print(min(sequence))

result = []
while sequence:
    current = sequence.pop()
    result.append(current)
print(*result, sep=", ")
