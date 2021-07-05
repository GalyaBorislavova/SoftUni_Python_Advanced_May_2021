def create_empty_triangle(size):
    triangle = []

    for r in range(size):
        triangle.append([0] * (r + 1))

    return triangle


def get_magic_triangle(size):
    magic_triangle = create_empty_triangle(size)

    magic_triangle[0][0] = 1
    for row in range(1, size):
        for col in range(len(magic_triangle[row])):
            first_up_cell = second_up_cell = 0
            if 0 <= row - 1 < len(magic_triangle) and 0 <= col < len(magic_triangle[row - 1]):
                first_up_cell = magic_triangle[row - 1][col]
            if 0 <= col - 1 < len(magic_triangle[row - 1]) and 0 <= row - 1 < len(magic_triangle):
                second_up_cell = magic_triangle[row - 1][col - 1]
            magic_triangle[row][col] = first_up_cell + second_up_cell

    print(magic_triangle)
    return magic_triangle


get_magic_triangle(5)
