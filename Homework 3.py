def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c


print(my_func(int(input('Введите 1 число: ')), int(input('Введите 2 число:')), int(input('Введите 3 число:'))))

