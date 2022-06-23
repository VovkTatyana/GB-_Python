def sum_result():
    f = 0
    while True:
        user_enter = input('Введите целые числа, через пробел: ').upper().split()
        for i in user_enter:
            if user_enter == 'Q':
                break
            try:
                f += int(i)
            except ValueError:
                print('Неверный тип, учитываем только целые числа')
        else:
            print(f)
            continue
        break
    return f


print(sum_result())

