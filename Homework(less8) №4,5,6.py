class Warehouse:
    pass


class Appliances:

    def __init__(self, name, use_time, amount):
        self.name = name
        self.use_time = use_time
        self.amount = amount
        self.p_dep = {'open_space': 0, 'accounting': 0, 'secretar': 0}
        self.s_dep = {'open_space': 0, 'accounting': 0, 'secretar': 0}
        self.x_dep = {'open_space': 0, 'accounting': 0, 'secretar': 0}

    def parameters(self):
        return f'Наименование:{self.name}, срок службы {self.use_time} год(а), кол-во на складе:{self.amount} шт.'


class Printer(Appliances):

    def receive(self, received):
        self.amount += received
        return f' После поставки, на складе стало {self.amount}'

    def left(self, send, department):

        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.p_dep[department] += send
            return f' После отправки на складе осталось {self.amount} в отделе сейчас {self.p_dep[department]}'
        elif str(send).isdigit() and self.amount < send:
            return 'Мы не можем столько предоставить'
        else:
            return 'Введите число!'

    def what_doing(self):
        return 'Печатает'

class Scanner(Appliances):

    def receive(self, received):
        self.amount += received
        return f' После поставки, на складе стало {self.amount}'

    def left(self, send, department):
        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.s_dep[department] += send
            return f' После отправки на складе осталось {self.amount} в отделе сейчас {self.s_dep[department]}'
        elif str(send).isdigit() and self.amount < send:
            return 'Мы не можем столько предоставить '
        else:
            return 'Введите число!'

    def what_doing(self):
        return 'Сканирует'

class Xerox(Appliances):

    def receive(self, received):
        self.amount += received
        return f' После поставки, на складе стало {self.amount}'

    def left(self, send, department):
        if str(send).isdigit() and self.amount >= send:
            self.amount -= send
            self.x_dep[department] += send
            return f' После отправки на складе осталось {self.amount} в отделе сейчас {self.x_dep[department]}'
        elif str(send).isdigit() and self.amount < send:
            return 'Мы не можем столько предоставить '
        else:
            return 'Введите число!'

    def what_doing(self):
        return 'Копирует'


my_printer = Printer
print(my_printer.what_doing(Printer))
my_scanner = Scanner
print(my_scanner.what_doing(Scanner))
my_xerox = Xerox
print(my_xerox.what_doing(Xerox))

my_printer = Printer('Принтер', 2, 20)
print(my_printer.parameters())
my_scanner = Scanner('Сканер', 6, 5)
print(my_scanner.parameters())
my_xerox = Xerox('Ксерокс', 1, 48)
print(my_xerox.parameters())

print(my_printer.receive(5))
print(my_scanner.receive(10))
print(my_xerox.receive(24))


print(my_printer.left(8, 'open_space'))
print(my_scanner.left(1, 'accounting'))
print(my_xerox.left(4, 'secretar'))

print(my_printer.left(7, 'open_space'))
print(my_scanner.left(6, 'accounting'))
print(my_xerox.left(24, 'secretar'))

print(my_printer.left(7, 'open_space'))
print(my_scanner.left(100, 'accounting'))
print(my_xerox.left('hnjmk', 'secretar'))




