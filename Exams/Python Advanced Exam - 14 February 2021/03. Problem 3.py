def stock_availability(inventory: list, action, *args):
    if action == "delivery":
        for product in args:
            inventory.append(product)
    elif action == "sell":
        args = list(args)
        if not args:
            if inventory:
                inventory.pop(0)
        else:
            if str(args[0]).isdigit():
                for product in range(args[0]):
                    if inventory:
                        inventory.pop(0)
            else:
                for order in args:
                    if order in inventory:
                        inventory = list(filter(order.__ne__, inventory))

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 30))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
