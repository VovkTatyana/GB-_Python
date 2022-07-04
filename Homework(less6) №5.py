class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

paint_1 = Pencil('карандашом')
paint_1.draw()
paint_2 = Pen('ручкой')
paint_2.draw()
paint_3 = Handle('маркером')
paint_3.draw()
