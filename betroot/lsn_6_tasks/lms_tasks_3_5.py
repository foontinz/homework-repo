import random

if __name__ == '__main__':
    # В цикле пока пользователь не введет Q запрашивайте Фамилии игроков.
    # Сложите их в лист. Отсортируйте лист используя втсроенную функцию. Выведите на экран получившийся список.

    answer = ''
    player_list = []
    while answer.lower() != 'q':
        answer = input('Введите фамилию игрока')
        if answer.lower() != 'q':
            player_list.append(answer.lower().capitalize())
    player_list.sort()
    print(player_list)

    if len(player_list) % 2 != 0:
        print(f'{player_list[-1]} проходит в следующий раунд без боя')
        player_list.pop()

    for i in range(1, int(len(player_list) / 2 + 1)):
        print(f'{player_list[i - 1]} играет c {player_list[-i]}')

    # Выглядит страшновато, пишу под ночь (вероятно есть попроще все эт)

    # Generate 2 lists with the length of 10 with random integers from 1 to 10,
    # and make a third list containing the common integers between the 2 initial lists without any duplicates.

    my_list_1 = [random.randrange(1, 10) for x in range(10)]
    my_list_2 = [random.randrange(1, 10) for x in range(10)]
    # думал думал, выгуглил comprehensions удобная тема но сложночитаемая как по мне)
    sorted_list = []
    for i in range(10):
        if i in my_list_2 and i in my_list_1:
            sorted_list.append(i)
    print(f'{sorted_list} - sorted list')

    # Make a list that contains all integers from 1 to 100,
    # then find all integers from the list that are divisible by 7 but not a multiple of 5,
    # and store them in a separate list. Finally, print the list.
    listok = list(range(100))
    listok_2 = []
    i = 0
    while i < len(listok):
        if listok[i] % 5 and not listok[i] % 7:
            listok_2.append(listok[i])
        i += 1
    print(listok_2)
