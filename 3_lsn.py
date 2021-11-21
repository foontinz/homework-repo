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

    #Задание У вас есть переменные holiday, day_of_week, wallet проставьте условия в код.
    #Попробуйте менять исходные значения чтоб убедиться что все ok
    holiday, day_of_week_2, wallet = False, 6, 5000
    beer , chipsiki , restik, polet = 1000, 500, 2500, 5000
    if (holiday==True or 6<=day_of_week_2<=7) and (wallet<chipsiki):
        print("оно то и можно погулять но не на что")
    elif (wallet==chipsiki+beer):
        print("пиво и чипсы на большее денег нет")
    elif (wallet>=restik and (holiday==True or 6<=day_of_week_2<=7)):
        print("гуляем в ресторане, всех угощаю")
    elif (wallet>=polet and (holiday==True or 6<=day_of_week_2<=7)):
        print("После Безоса следующим лечу я. И моя любимая кошка!")
    else:
        print("работаем")

