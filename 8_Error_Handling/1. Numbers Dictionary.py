numbers_dictionary = {}

while True:
    data = input()

    if data == "Search":
        break

    value = input()

    if value == "Search":
        break

    key = data
    try:
        number = int(value)
        numbers_dictionary[key] = number
    except Exception:
        print("The variable number must be an integer")


while True:
    data = input()

    if data == "Remove":
        break
    key = data
    print(numbers_dictionary.get(key, "Number does not exist in dictionary"))

while True:
    data = input()

    if data == "End":
        break

    searched = data
    try:
        del numbers_dictionary[searched]
    except Exception:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
