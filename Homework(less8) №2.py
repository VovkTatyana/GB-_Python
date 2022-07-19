class MyError(Exception):
    pass

x = int(input("Введите число которое вы хотите разделить: "))
y = int(input("Введите число на которое вы хотите разделить: "))

try:
    if y == 0:
        raise MyError("На 0 делить нельзя!")

except MyError as mr:
    print(mr)
else:
    print(x/y)
