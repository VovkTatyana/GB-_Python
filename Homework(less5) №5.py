with open('text_5.txt', 'w+', encoding='utf-8') as f:
    user_enter = input('Введите числа, через пробел, для суммирования: ')
    f.write(str(user_enter))
    f.seek(0)
    print(sum(map(int, f.read().split())))

