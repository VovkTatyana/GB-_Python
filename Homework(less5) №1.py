user_list = input('Введите данные: ')
with open("homework№1.txt", "w", encoding='utf-8') as file:
    for line in user_list:
        file.writelines(user_list + '\n')

