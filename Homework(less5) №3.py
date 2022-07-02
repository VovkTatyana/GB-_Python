last_name = []
all_income = 0
employees = 0
with open("text_3.txt", 'r', encoding='utf-8') as f:
    for line in f:
        employees += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            last_name.append(name)
        all_income += income
    all_income /= employees
print('Сотрудники с окладом менее 20 000:')
print(*last_name, sep=",")
print('Средний оклад сотрудника фирмы равен', all_income, 'руб.')

