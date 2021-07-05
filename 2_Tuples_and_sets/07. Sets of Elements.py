def first_set_numbers(count):
    a = set()
    for _ in range(count):
        num = input()
        a.add(num)
    return a


def second_set_numbers(count):
    b = set()
    for _ in range(count):
        num = input()
        b.add(num)
    return b


def print_intersection_elements_in_two_sets(a, b):
    intersection_of_sets = a.intersection(b)
    for num in intersection_of_sets:
        print(num)


n, m = [int(el) for el in input().split(" ")]
first_set = first_set_numbers(n)
second_set = second_set_numbers(m)
intersection = first_set.intersection(second_set)
print_intersection_elements_in_two_sets(first_set, second_set)