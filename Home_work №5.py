numbers = [9, 7, 7, 6, 4, 4, 1]
user_enter = input('Enter new number: ')

if user_enter in numbers:
    index = numbers.rfind(user_enter)
    numbers.insert((index + 1), int(user_enter))
    print(numbers)
else:
    numbers.append(int(user_enter))
    numbers.sort(reverse=True)
    print(numbers)
