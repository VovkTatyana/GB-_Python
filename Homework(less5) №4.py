my_dict = dict(One='Один', Two='Два', Three='Три', Four='Четыре')
with open("text_4.txt", 'r', encoding='utf-8') as f:
    with open("my_text_4.txt", 'w', encoding='utf-8') as f2:
        for line in f:
            en, *num = line.split()
            ru = my_dict[en]
            f2.write(''.join([ru] + num) + '\n')

