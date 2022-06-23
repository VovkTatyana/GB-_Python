a = 2
b = 3
day = 1
print(day, 'th day:', a)
while a <= b:
    day += 1
    a *= 1.1

    print(day, 'th day:', round(a, 2))
if a >= b:
    print(f'On the {day} th day, the athlete reached the result - at least 3 km.')


