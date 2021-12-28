import argparse
import os

log_mess = ['login', 'l', 'log', ]
reg_mess = ['reg', 'register', 'r']
LOGGED = False


def check_db():
    return os.path.exists(os.path.join(os.getcwd(), 'log_pass.txt'))


def create_db():
    with open('log_pass.txt', 'w') as write_db:
        write_db.write('')


def read_data():
    if check_db():
        with open('log_pass.txt', 'r') as read_db:
            data = read_db.readlines()
        return data
    else:
        create_db()
        return read_data()


def log_check(name, login, password):
    data = read_data()
    for i in data:
        i = i.split(';')
        if name == i[0] and login == i[1] and password == i[2]:
            return True
    return False


def register(info):
    data = read_data()
    for i in data:
        i = i.split(';')
        if info[1] is i[1]:
            print('Логин занят')
            return register(ask_log())
    info = ';'.join(info) + '\n'
    with open('log_pass.txt', 'a') as write_db:
        write_db.write(info)
    return 'Ваш аккаунт бын внесён в базу'


def ask_log():
    name = input('Input your name')
    log = input('Input your login')
    password = input('Input your password')
    return [name, log, password]


if __name__ == '__main__':

    parser = argparse.ArgumentParser('l/r?')
    parser.add_argument('L_R', type=str, help='What you want? log/reg')
    args = parser.parse_args()

    if (args.L_R) in log_mess:
        while LOGGED != True:
            LOGGED = log_check(*ask_log())
    elif (args.L_R) in reg_mess:
        print(register(ask_log()))
