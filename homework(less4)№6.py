from itertools import count, cycle

my_list = []
for el in count(3):
    my_list.append(el)
    if el == 6:
        break
print(my_list)

for i, j in enumerate(cycle(my_list)):
    print(j, end=' ')
    if i == 9:
        break
print()

