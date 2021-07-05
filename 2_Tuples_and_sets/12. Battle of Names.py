n = int(input())

even_set = set()
odd_set = set()

for count_line_iteration in range(1, n + 1):
    current_sum_name = sum([ord(char) for char in input()]) // count_line_iteration
    if current_sum_name % 2 == 0:
        even_set.add(current_sum_name)
    else:
        odd_set.add(current_sum_name)


if sum(even_set) == sum(odd_set):
    result = [str(el) for el in even_set.union(odd_set)]
elif sum(even_set) < sum(odd_set):
    result = [str(el) for el in odd_set.difference(even_set)]
else:
    result = [str(el) for el in even_set.symmetric_difference(odd_set)]
print(', '.join(result))