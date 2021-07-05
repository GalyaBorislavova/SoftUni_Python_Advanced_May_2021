def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        if " " in line:
            data = line.split()
            for el in data:
                lines.append(el)
        else:
            lines.append(line)
    return lines


def add_chemical_element_into_set(elements):
    table_of_unique_chem_elements = set()
    for el in elements:
        table_of_unique_chem_elements.add(el)
    return table_of_unique_chem_elements


def print_element_in_periodic_table(table):
    for element in table:
        print(element)


n = int(input())
input_chemical_elements = input_to_list(n)
periodic_table = add_chemical_element_into_set(input_chemical_elements)
print_element_in_periodic_table(periodic_table)