data = input().split("|")[::-1]

new_list = [[el for el in el.strip().split()] for el in data]

print(' '.join(sum(new_list, [])))