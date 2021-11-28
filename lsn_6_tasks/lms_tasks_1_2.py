import random

if __name__ == '__main__':

    # Рандом и расширение списка.
    my_list = []
    while len(my_list) != 10:
        my_list.append(random.randint(1, 100))
    print(my_list)

    maximum = minimum = my_list[0]

    for i in my_list:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    print(maximum, minimum)


    #Превратите полученную от пользователя строку в тапл. Выведите строку содержащую только буквы на четных позициях.

    string = tuple(input('ENTER STRING'))
    word = ''
    for i in range(len(string)):
        if not i%2:
            word = word + string[i]
    print(word)

