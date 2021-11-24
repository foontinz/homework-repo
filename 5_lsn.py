import random

if __name__ == '__main__':
    i = 0
    pc_wins = 0
    person_wins = 0
    print('''rock = 1
scizors = 2
paper = 3''')
    amount_rounds = 0
    while amount_rounds%2==0:
        amount_rounds = int(input('How much rounds you want? not even'))

    while i < amount_rounds:
        i += 1
        number = random.randint(1, 3)
        ans = 'qqq'

        while ans != '1' and ans != '2' and ans != '3':
            ans = input('Choose rock,paper or scizzors')
        ans = int(ans)
        if ans == number:
            i -= 1
            continue
        if (ans == 1 and number == 2) or (ans == 2 and number == 3) or (ans == 3 and number == 1):
            person_wins += 1
            print('You wins round')
        else:
            pc_wins += 1
            print('Pc wins round')
        a = max(pc_wins,person_wins)
        if a > amount_rounds/2:
            break
    if pc_wins>person_wins:
        print('Pc wins')
    else:
        print('Person wins')