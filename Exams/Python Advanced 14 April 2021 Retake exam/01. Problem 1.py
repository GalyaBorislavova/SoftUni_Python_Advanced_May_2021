from collections import deque


def valid_order(numbers_of_pizza):
    return 0 < numbers_of_pizza < 11


def complete_order(count_order_pizzas, capacity_employee):
    return capacity_employee >= count_order_pizzas


def remaining_order(count_pizza, capacity_employee):
    return count_pizza - capacity_employee


pizza_orders = deque(list(filter(valid_order, [int(n) for n in input().split(", ")])))
employees = [int(x) for x in input().split(", ")]

total_count_pizza = 0
complete_all_orders = True

while pizza_orders:
    if not complete_all_orders:
        break
    if employees:
        current_order = pizza_orders.popleft()
        current_employee = employees.pop()

        if complete_order(current_order, current_employee):
            total_count_pizza += current_order
            continue

        else:
            remaining_count_pizza = remaining_order(current_order, current_employee)
            if employees:
                if complete_order(remaining_count_pizza, employees.pop()):
                    total_count_pizza += current_order
                    continue
            elif remaining_count_pizza > 0 and not employees:
                pizza_orders.appendleft(remaining_count_pizza)
                complete_all_orders = False
                break
            else:
                complete_all_orders = False
                break
    else:
        complete_all_orders = False
        break


if complete_all_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count_pizza}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizza_orders])}")

