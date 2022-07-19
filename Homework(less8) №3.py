class MyError():

    def My_list():
        my_list = []
        while True:
            user_enter = input('Введите числa которое вы хотите добавить в список: ')
            if user_enter.isdigit():
                my_list.append(user_enter)
            elif user_enter.lower() == 'stop':
                print(my_list)
                break

            else:
                print('Введите число!')


nun = MyError
nun.My_list()
