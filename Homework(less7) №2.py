from abc import ABC, abstractmethod


class Clothes(ABC):
    fabric_consumption = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.fabric_consumption += self.consumption

    def __str__(self):
        return f'На пальто {self.size} размера израсходованно {self.consumption} м. ткани, общий расход ткани на пальто {Coat.fabric_consumption:.2f} м.'

    @property
    def consumption(self):
        con = self.size / 6.5 + 0.5
        return float(f'{con:.2f}')


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.fabric_consumption += self.consumption

    def __str__(self):
        return f'Костюм на рост {self.height} см., расход ткани {self.consumption} м., общий расход ткани на пошив костюмов {Suit.fabric_consumption :.2f} м. '

    @property
    def consumption(self):
        con = (self.height * 2 + 0.3) / 100
        return float(f'{con:.2f}')


cloth_1 = Coat(55)
print(cloth_1)
cloth_2 = Coat(48)
print(cloth_2)
cloth_3 = Suit(170)
print(cloth_3)
cloth_4 = Coat(50)
print(cloth_4)
cloth_5 = Suit(178)
print(cloth_5)

