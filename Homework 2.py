def hi(**kwargs):
    print('Привет, давай знакомиться!)')
    name = input('Как тебя зовут?: ')
    last_name = input('Напиши свою фамилию: ')
    birth = input('В каком году ты родился?: ')
    sity = input('Где живёшь?: ')
    email = input('Введи свой email, что бы я мог тебе написать): ')
    phone = input('И телефон: ')
    return print(
        f'Супер, резюмирую. Тебя зовут {name} {last_name} ты родил(ся/ась) в {birth} году, живешь в городе {sity} и твои контактные данные {email} и {phone} ')


print(hi())

