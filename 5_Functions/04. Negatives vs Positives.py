def is_positive(num):
    return num >= 0


def is_negative(num):
    return num < 0


numbers = [int(x) for x in input().split()]

positives = filter(is_positive, numbers)
negatives = filter(is_negative, numbers)

sum_positives = sum(positives)
sum_negatives = sum(negatives)

print(sum_negatives)
print(sum_positives)

if sum_positives < abs(sum_negatives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")