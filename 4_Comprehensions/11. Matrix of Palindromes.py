r, c = [int(x) for x in input().split()]

palindrome_matrix = []

i = 97
for row in range(r):
    palindrome_matrix.append([])
    for col in range(c):
        palindrome_matrix[row].append(f"{chr(i+row)}{chr(i+row+col)}{chr(i+row)}")

for rows in palindrome_matrix:
    print(*rows, sep=" ")