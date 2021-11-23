if __name__ == '__main__':
    # Git tasks ⟱⟱⟱:
    # Допишите код так, чтобы меняя значение переменной day_of_week выводились следующие сообщения ʼрабочий деньʼ, 'выходной', 'Ошибка!
    # Дни недели считаются 1-7 ни больше ни меньше!'
    day_of_week = 11
    if (1 >= day_of_week <= 5):
        print('Рабочий день')
    elif (5 >= day_of_week <= 7):
        print('Выходной')
    else:
        print('¯\_ (ツ) _/¯ \n')

    # Задание У вас есть переменные holiday, day_of_week, wallet проставьте условия в код.
    # Попробуйте менять исходные значения чтоб убедиться что все ok
    holiday, day_of_week_2, wallet = False, 6, 5000
    beer, chipsiki, restik, polet = 1000, 500, 2500, 5000
    if (holiday == True or 6 <= day_of_week_2 <= 7) and (wallet < chipsiki):
        print("оно то и можно погулять но не на что")
    elif (wallet == chipsiki + beer) and (holiday == True or 6 <= day_of_week_2 <= 7):
        print("пиво и чипсы на большее денег нет")
    elif (wallet >= restik and (holiday == True or 6 <= day_of_week_2 <= 7)):
        print("гуляем в ресторане, всех угощаю")
    elif (wallet >= polet and (holiday == True or 6 <= day_of_week_2 <= 7)):
        print("После Безоса следующим лечу я. И моя любимая кошка!")
    else:
        print("работаем")

    # задание Выведите значения у для х в пределах от 0 до 100 c шагом 1 если y = 3x + 12
    x = 0
    for i in range(-1, 100):
        y = 3 * x + 12
        print(f'x={x}, y={y} \n')
        x += 1

    # Провалидируйте введенный пользователем номер телефона.

    phone_number = '+0672937803'
    if (phone_number[0:1] == '+'):
        if (phone_number[1:4] == '067' or phone_number[1:4] == '039' or phone_number[1:4] == '068'):
            print('Kyivstar')
        elif (phone_number[1:4] == '063' or phone_number[1:4] == '093'):
            print('Lifecell')
        elif (phone_number[1:4] == '050' or phone_number[1:4] == '066' or phone_number[1:4] == '095'):
            print('MTS')
        else:
            print('Какой нибудь другой)')
    else:
        if (phone_number[0:3] == '067' or phone_number[0:3] == '039' or phone_number[0:3] == '068'):
            print('Kyivstar')
        elif (phone_number[0:3] == '063' or phone_number[0:3] == '093'):
            print('Lifecell')
        elif (phone_number[0:3] == '050' or phone_number[0:3] == '066' or phone_number[0:3] == '095'):
            print('MTS')
        else:
            print('Какой нибудь другой)')

    # Используя функцию input получаем от пользователя строку. Напишите код в котором просим дать ответ на загадку.
    # Если человек сдается он вводит q или Q и прерываем цикл while. Если угадал - выводим поздравление. Если нет - пристыдите его.
    # Ответ принимается регистронезависимо.

    question = 'Маленькое беленькое на потолко висит не светит'
    answer = 'лампачка'
    while True:
        ans = input('Маленькое беленькое на потолко висит не светит. Что это?').lower()
        if (ans == answer):
            print('Congratulations!!!')
            break
        elif (ans == 'q'):
            break
        else:
            print('Неа')

