class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        print('\n'.join(map(str, self.my_list)))

    def __add__(self, my_list_2):
        new = []
        if len(self.my_list) != len(my_list_2.my_list) or len(self.my_list[0]) != len(my_list_2.my_list[0]):
            print('Введите одинаковые матрицы!')
        else:
            for i in range(len(self.my_list)):
                new.append([])
                for el in range(len(self.my_list[0])):
                    new[i].append(self.my_list[i][el] + my_list_2.my_list[i][el])
        print('\n'.join(map(str, new)))


list_1 = [[1, 2], [3, 3], [5, 6]]
list_2 = [[1, 5], [6, 6], [7, 9]]
my_list_1 = Matrix(list_1)
my_list_2 = Matrix(list_2)
my_list_1.__add__(my_list_2)
