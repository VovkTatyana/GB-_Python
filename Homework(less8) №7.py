class Complex_number:

    def __init__(self, real, comp):
        self.real = real
        self.comp = comp

    def __str__(self):
        sign = '+' if self.comp >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.comp)

    __repr__ = __str__


class ComplexCalculate:

    def add(self, c1, c2):
        real = c1.real + c2.real
        comp = c1.comp + c2.comp
        return Complex_number(real, comp)

    def mul(self, c1, c2):
        real = c1.real * c2.real - c1.comp * c2.comp
        comp = c1.comp * c2.real + c1.real * c2.comp
        return Complex_number(real, comp)


calc = ComplexCalculate()
print(calc.add(Complex_number(4, 3), Complex_number(7, 5)))
print(calc.mul(Complex_number(8, 1), Complex_number(2, 4)))
