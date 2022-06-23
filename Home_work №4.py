user_enter = input('Введите несколько слов, через пробел: ').split()

for i, word in enumerate(user_enter, 1):
    print(i, word[:10])

