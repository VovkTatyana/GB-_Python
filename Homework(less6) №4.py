class Car:


    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def police(self):
        is_police = False
        print(is_police)

    def go(self):
        print(f'{self.name} drove off!')


    def stop(self):
        print(f'{self.name} stopped!')


    def turn_left(self):
        print(f'{self.name} turn on the left')


    def turn_right(self):
        print(f'{self.name} turn on the right')

    def show_speed(self):
        print(f'{self.name} is going {self.speed}')


class TownCar(Car):
    def car_type(self):
        print('This is Town car')
    def show_speed(self):
        print(f'{self.name} is going {self.speed}')
        if self.speed > 60:
            print('OVER SPEED!')


class SportCar(Car):
    def car_type(self):
        print('This is Sport car')


class WorkCar(Car):
    def car_type(self):
        print('This is Work car')
    def show_speed(self):
        print(f'{self.name} is going {self.speed} ')
        if self.speed > 40:
            print('OVER SPEED!')


class PoliceCar(Car):
    def police(self):
        is_police = True
        print(is_police)


avto_1 = TownCar(70, 'red', 'Audi')
avto_1.show_speed()
avto_1.car_type()
avto_2 = SportCar(90, 'black', 'BMW')
avto_2.go()
avto_2.police()
avto_2.turn_left()
avto_3 = PoliceCar(60, 'blue', 'Ford')
avto_3.police()
