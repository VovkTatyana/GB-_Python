class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


worker_1 = Position('Tatyana', 'Vovk', 'Manager', 100000, 50000)

print(f'{worker_1.position}: {worker_1.get_full_name()}, пролный оклад с учетом премии равен {worker_1.get_total_income()}')
worker_2 = Position('Ivan', 'Ivanov', 'Manager', 90000, 25000)
print(f'{worker_2.position}: {worker_2.get_full_name()}, пролный оклад с учетом премии равен {worker_2.get_total_income()}')
