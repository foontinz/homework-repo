# Допишите игру 21.
from random import choice
from random import randint


def random_card():
    index_deck = randint(0, 3)
    index_para = randint(0, 12)
    part_of_deck = FULL_DECK.pop(index_deck)
    for s, v in part_of_deck.items():
        suit = s
        values = v
    para = values.pop(index_para)
    FULL_DECK.append(part_of_deck)
    for m, v in para.items():
        mark = m
        value = v
    return [mark,suit,value]


def deposit(balance: int):
    while True:
        try:
            balance += int(input('Enter amount of your deposit in UAH'))
        except:
            print('Wrong format, dude')
            continue
        return balance


def deck_shuffle(DECK):
    pass


if __name__ == '__main__':
    FULL_DECK = [
        {'♠': [{'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 10},
               {'Q': 10}, {'K': 10}, {'A': 11}]},
        {'♥': [{'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 10},
               {'Q': 10}, {'K': 10}, {'A': 11}]},
        {'♣': [{'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 10},
               {'Q': 10}, {'K': 10}, {'A': 11}]},
        {'♦': [{'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 10},
               {'Q': 10}, {'K': 10}, {'A': 11}]}]
    MONEY_BALANCE = 0
    PLAYER_POINTS = 0
    DEALER_POINTS = 0

    while True:
        start = input('Wanna play ? (y/n)').lower().strip()
        if start == 'y':
            start = True
            break
        elif start == 'n':
            start = False
            break
        print('Wrong format dude')
        continue

    #while start is True:
    name = input('Say your name please')
    print(f'Hi, Mr {name}, game is starting ')
    round_1_player_1 = random_card()
    round_1_player_2 = random_card()
    round_1_dealer_1 = random_card()
    round_1_dealer_2 = random_card()
    PLAYER_POINTS = round_1_player_1[2] + round_1_player_2[2]
    DEALER_POINTS = round_1_dealer_1[2] + round_1_dealer_2[2]