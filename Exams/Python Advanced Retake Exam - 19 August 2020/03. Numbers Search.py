def numbers_searching(*args):
    args_as_list = [int(el) for el in args]
    max_number = max(args_as_list)
    min_number = min(args_as_list)
    missing_number = [num for num in range(min_number, max_number + 1) if num not in args_as_list][-1]
    duplicates = set([num for num in args if args.count(num) > 1])
    sort_duplicates = sorted(list(duplicates))
    result = [missing_number, sort_duplicates]

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
