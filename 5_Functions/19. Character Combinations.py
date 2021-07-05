from itertools import permutations

data = input()
result = permutations(data)

for lists in result:
    print(''.join(list(lists)))


