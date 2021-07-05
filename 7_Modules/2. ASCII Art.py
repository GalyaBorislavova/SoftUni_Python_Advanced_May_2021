from pyfiglet import figlet_format


def print_art(message):
    figure = figlet_format(message)
    print(figure)


data = input()
print_art(data)


