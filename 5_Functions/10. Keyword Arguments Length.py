def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
alphabet = {"a": 1, "b": 2, "c": 3}

print(kwargs_length(**dictionary))
print(kwargs_length(**alphabet))