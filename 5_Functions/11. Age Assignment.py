def age_assignment(*names, **ages):
    people = {}
    for name in names:
        first_letter = name[0]
        for letter, age in ages.items():
            if letter == first_letter:
                people[name] = age

    return people


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
