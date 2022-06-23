def my_f(num_1, num_2):
    try:
        return num_1//num_2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

print(my_f(int(input('Введите число которое хотите разделить: ')),int(input('Введите число на которое хотите разделить: '))))

