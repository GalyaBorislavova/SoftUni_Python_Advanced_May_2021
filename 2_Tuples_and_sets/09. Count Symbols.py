def elements_and_occurrences_in_dict(text):
    my_dict = {}
    for char in text:
        my_dict[char] = text.count(char)
    return my_dict


def print_occurrences(dict_with_symbols):
    for char, occ in dict_with_symbols:
        print(f"{char}: {occ} time/s")


input_text = input()
symbols = elements_and_occurrences_in_dict(input_text)

sorted_data = sorted(symbols.items(), key=lambda x: x[0])
print_occurrences(sorted_data)