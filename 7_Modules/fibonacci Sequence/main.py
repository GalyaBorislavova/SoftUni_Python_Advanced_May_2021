from create_and_find_functions import *

fibonacci_sequence = []
data = input()

while not data == "Stop":
    command, *rest = data.split()

    if command == "Create":
        number = int(rest[-1])
        fibonacci_sequence = create_fibonacci_sequence(number)
        print(*fibonacci_sequence)
    elif command == "Locate":
        number = int(*rest)
        result = find_num_in_fibonacci_seq(number, fibonacci_sequence)
        print(f"The number - {number} is at index {result}"
              if isinstance(result, int) else result)

    data = input()
