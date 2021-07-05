numbers = [int(x) for x in input().split(", ")]

positives = [n for n in numbers if n >= 0]
negatives = [n for n in numbers if n < 0]
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 == 1]

print("Positive:", ', '.join([str(n) for n in positives]))
print("Negative:", ', '.join([str(n) for n in negatives]))
print("Even:", ', '. join([str(n) for n in evens]))
print("Odd:", ', '.join([str(n) for n in odds]))