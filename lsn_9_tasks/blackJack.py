# Допишите игру 21.
from random import choice
from random import randint


def make_bet(balance):
    current_bet = input('Make bet, use only digits pls')
    try:
        current_bet = int(current_bet)
        balance -= current_bet
        return current_bet, balance
    except:
        print('Wrond format, dude')
        make_bet(balance)


def check_21(p_points, d_points):
    if d_points == 21:
        return False, True
    elif p_points == 21:
        return True, False
    elif p_points > 21 and d_points <= 21:
        return False, True
    elif d_points > 21 and p_points <= 21:
        return True, False
    elif d_points > 21 and p_points > 21:
        return True, True
    else:
        return False, False


def get_name():
    name = input('Say your name please')
    return name


def first_round(p_points: int, d_points: int):
    round_1_player_1 = random_card()
    round_1_player_2 = random_card()
    round_1_dealer_1 = random_card()
    round_1_dealer_2 = random_card()
    p_points = round_1_player_1[2] + round_1_player_2[2]
    d_points = round_1_dealer_1[2] + round_1_dealer_2[2]
    print(f'Ваши карты {round_1_player_2[:2]} и {round_1_player_1[:2]}')
    print(f'Карты диллера {round_1_dealer_2[:2]} и {round_1_dealer_1[:2]}')
    return p_points, d_points


def random_card():
    index_deck = randint(0, 3)
    part_of_deck = FULL_DECK.pop(index_deck)
    for s, v in part_of_deck.items():
        suit = s
        values = v
    index_para = randint(0, len(values) - 1)
    para = values.pop(index_para)
    FULL_DECK.append(part_of_deck)
    for m, v in para.items():
        mark = m
        value = v
    return [mark, suit, value]


def deposit(balance: int):
    while True:
        try:
            balance += int(input('Enter amount of your deposit in UAH'))
        except:
            print('Wrong format, dude')
            continue
        return balance


def want_more(p_points, d_points):
    w_more = input('Want more? y/n').lower().strip()
    if w_more == 'y':
        w_more = True
        return w_more
    elif w_more == 'n':
        w_more = False
        return w_more
    else:
        print('Wrong format, dude')
        want_more(p_points, d_points)


def next_round(p_points: int, d_points: int):
    p_card = random_card()
    p_points += p_card[2]
    print(f'Вашa картa {p_card[:2]} ')
    if randint(0,1):
        d_card = random_card()
        d_points += d_card[2]
        print(f'Картa диллера {d_card[:2]}')
        return p_points, d_points
    print(f'Диллер не взял карту')
    return p_points, d_points


if __name__ == '__main__':
    FULL_DECK = [
        {'♠': [{'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 2}, {'Q': 3}, {'K': 4}, {'A': 11}]},
        {'♥': [{'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 2}, {'Q': 3}, {'K': 4}, {'A': 11}]},
        {'♣': [{'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 2}, {'Q': 3}, {'K': 4}, {'A': 11}]},
        {'♦': [{'6': 6}, {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 2}, {'Q': 3}, {'K': 4}, {'A': 11}]}]
    DEALER_WIN = False
    PLAYER_WIN = False

    MONEY_BALANCE = 0
    PLAYER_POINTS = 0
    DEALER_POINTS = 0

    NAME = get_name()
    while True:
        start = input(f'Wanna play, Mr {NAME} ? (y/n)').lower().strip()
        if start == 'y':
            start = True
            break
        elif start == 'n':
            start = False
            break
        print('Wrong format dude')
        continue

    if start is True:
        print(f'Mr {NAME}, game is starting')
        if MONEY_BALANCE == 0:
            MONEY_BALANCE = deposit(MONEY_BALANCE)
        CURRENT_BET, MONEY_BALANCE = make_bet(MONEY_BALANCE)
        print(f'Your bet is {CURRENT_BET}, remaining balance {MONEY_BALANCE}')

        PLAYER_POINTS, DEALER_POINTS = first_round(PLAYER_POINTS, DEALER_POINTS)

        while PLAYER_WIN != True and DEALER_WIN != True:
            print(PLAYER_POINTS, 'player', DEALER_POINTS, 'dealer')
            PLAYER_WIN, DEALER_WIN = check_21(PLAYER_POINTS, DEALER_POINTS)
            if PLAYER_WIN and DEALER_WIN:
                MONEY_BALANCE += CURRENT_BET
                print(f'Draw, your balance now \t{MONEY_BALANCE}')
            elif PLAYER_WIN is True:
                MONEY_BALANCE += CURRENT_BET * 2
                print(f'You won, your balance now \t{MONEY_BALANCE}')
                break
            elif DEALER_WIN is True:
                print(f'You lost, your balance now\t{MONEY_BALANCE}')
                break
            else:
                w_more = want_more(PLAYER_POINTS, DEALER_POINTS)
                if w_more:
                    PLAYER_POINTS, DEALER_POINTS = next_round(PLAYER_POINTS, DEALER_POINTS)
                    continue
                elif not w_more:
                    if PLAYER_POINTS > DEALER_POINTS:
                        MONEY_BALANCE += CURRENT_BET * 2
                        print(f'You won, your balance now {MONEY_BALANCE}')
                        break
                    else:
                        print(f'You lost, your balance now{MONEY_BALANCE}')
                        break
