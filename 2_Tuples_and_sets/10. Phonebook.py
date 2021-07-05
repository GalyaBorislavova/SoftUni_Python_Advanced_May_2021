def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def check_and_print_names(p_book, names):
    for name in names:
        if name in p_book:
            print(f"{name} -> {p_book[name]}")
        else:
            print(f"Contact {name} does not exist.")


def adding_contact_in_phonebook(p_book, contact_name, phone):
    p_book[contact_name] = phone
    return p_book


phonebook = {}

data = input()

while not data.isdigit() == True:
    name, number = data.split("-")
    phonebook = adding_contact_in_phonebook(phonebook, name, number)
    data = input()
else:
    n = int(data)
    names_to_check = input_to_list(n)
    check_and_print_names(phonebook, names_to_check)

