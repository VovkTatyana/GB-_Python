class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        print(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums > other.nums:
            print(self.nums - other.nums)
        else:
            print('Error!')

    def __mul__(self, other):
        print(self.nums * other.nums)

    def __truediv__(self, other):
        print(self.nums // other.nums)

    def make_order(self, cell_len):
        self.cell_len = cell_len
        count = self.nums
        my_str = ''
        while count >= self.cell_len:
            count -= self.cell_len
            my_str += (('*' * self.cell_len) + '\n')
            continue
        if count < self.cell_len:
            my_str += ('*' * count)
        print(my_str)


enter = Cell(12)
my_enter = Cell(5)
enter.__add__(my_enter)
enter.__sub__(my_enter)
enter.__truediv__(my_enter)
enter.__mul__(my_enter)
