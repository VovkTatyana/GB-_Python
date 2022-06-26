def fact_func(num):
    f_num = 1
    for i in range(1, num + 1):
        f_num *= i
        yield f'{i}! = {f_num}'


for el in fact_func(int(input('Факториал: '))):
    print(f'Факториал {el}')

