with open('Homework(less5)№2.txt', 'r', encoding='utf-8') as f:
    count = len(open('Homework(less5)№2.txt').readlines())
    print('Всего в файле', count, 'строки')
    my_line = f.readlines()
    for i, v in enumerate(my_line, 1):
        words = len(v.split())
        print(f'{i}-я строка содержит {words} слово/а')

