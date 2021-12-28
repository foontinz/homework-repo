import random

if __name__ == '__main__':
    # Words combination

    num = 5
    word = input('Enter word you want to combine')
    amount = len(word)
    for i in range(num):
        editing_word = word
        new_word = ''
        # print(editing_word)
        j = 0
        while j < amount:
            j += 1
            if len(editing_word) == 0:
                break
            index = random.randint(0, len(editing_word) - 1)
            # print(index, 'index')
            new_word = new_word + editing_word[index]
            # print(new_word, 'new word')
            editing_word = editing_word[:index] + editing_word[index + 1:]
            # print(editing_word, 'editing word')
        print(new_word)

        # Используя модуль random и его функции randint напишите игру "математика 5кл".

    while True:
        equation_rand = random.randint(1, 3)
        x = random.randint(0, 30)
        equation_1 = 'y = 2x + 3'
        equation_2 = 'y = 3x + 15'
        equation_3 = 'y = x + 7'
        equation_1_solution = str(2 * x + 3)
        equation_2_solution = str(3 * x + 15)
        equation_3_solution = str(x + 7)
        if equation_rand == 1:
            print(f'{equation_1} \nx = {x}')
            ans = input('y = ')
            if ans == equation_1_solution:
                print('Перемога')
                break
            else:
                print('Зрада')

        elif equation_rand == 2:
            print(f'{equation_2} \nx = {x}')
            ans = input('y =')
            if ans == equation_2_solution:
                print('Перемога')
                break
            else:
                print('Зрада')
        else:
            print(f'{equation_3} \nx = {x}')
            ans = input('y =')
            if ans == equation_3_solution:
                print('Перемога')
                break
            else:
                print('Зрада')
