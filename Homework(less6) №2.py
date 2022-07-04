class Road:

    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

    def Calculation(self):
        return f'Для вашей дороги необходимо использовать {self.length * self.width * 25 * 5 // 1000} тонн асфальта'


road_1 = Road(20, 5000)
print(road_1.Calculation())

