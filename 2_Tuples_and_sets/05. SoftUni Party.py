def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def input_to_list_until_command(end_command):
    lines = []
    command = input()
    while not command == end_command:
        lines.append(command)
        command = input()
    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def separated_onto_vip_and_regular(guests):
    vip = []
    regular = []
    for guest in guests:
        if is_vip_guest(guest):
            vip.append(guest)
        else:
            regular.append(guest)
    return sorted(vip), sorted(regular)


def print_result(guests):
    (vip, regular) = separated_onto_vip_and_regular(guests)
    print(len(guests))
    for guest in vip:
        print(guest)
    for guest in regular:
        print(guest)


n = int(input())
reservations = input_to_list(n)
guests_arrived = input_to_list_until_command("END")
guest_not_arrived = set(reservations).difference(guests_arrived)
print_result(guest_not_arrived)