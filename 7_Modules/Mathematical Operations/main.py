from mapper import mapper_operator

number_1, operator, number_2 = input().split()
number_1, number_2 = float(number_1), float(number_2)

print(f"{mapper_operator[operator](number_1, number_2):.2f}")