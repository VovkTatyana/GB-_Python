def my_f(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y > 0:
        return res
    else:
        return 1 / res


print(my_f(float(input('Введите положительное число x: ')),int(input('Введите целое отрицательное число y: '))))

