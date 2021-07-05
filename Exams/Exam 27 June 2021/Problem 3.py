def math_operations(*args, **kwargs):
    position_num = 1
    for num in args:
        if position_num == 1:
            kwargs["a"] += num
        elif position_num == 2:
            kwargs["s"] -= num
        elif position_num == 3:
            if num != 0:
                kwargs["d"] /= num
        elif position_num == 4:
            kwargs["m"] *= num

        if position_num == 4:
            position_num = 1
        else:
            position_num += 1

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
