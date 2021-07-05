def create_fibonacci_sequence(n):

    sequence = [0, 1]

    for num in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def find_num_in_fibonacci_seq(num, seq: list):
    if num in seq:
        return seq.index(num)
    else:
        return f"The number {num} is not in the sequence"


