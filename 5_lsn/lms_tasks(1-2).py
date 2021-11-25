import random

if __name__ == '__main__':

    # The Guessing Game.

    number = str(random.randint(1, 10))
    guessed = 0
    while number != guessed:
        guessed = input('Enter number between 1 and 10')
        if number == guessed:
            print('You`ve won')
            break
        else:
            print('Nope -_-')

    # The birthday greeting program .

    name = input('Enter your name')
    age = int(input('Enter your age'))
    print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")
