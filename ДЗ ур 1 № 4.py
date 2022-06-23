number = int(input('Enter the number: '))
result = -1
while number > 10:
    i = number % 10
    number //= 10
    if i > result:
        result = i
print(result)

