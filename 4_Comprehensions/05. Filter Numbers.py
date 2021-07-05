def divisible(number):
    for n in range(2, 11):
        if number % n == 0:
            return True
    return False


start = int(input())
end = int(input())

filter_matrix = [
    int(num)
    for num in range(start, end + 1)
    if divisible(num)
]
print(filter_matrix)