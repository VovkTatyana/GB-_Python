user_enter = input('Enter a list separated by a space: ').split()
for i in range(1, len(user_enter), 2):
    user_enter[i-1],user_enter[i] = user_enter[i], user_enter[i-1]
print(user_enter)
