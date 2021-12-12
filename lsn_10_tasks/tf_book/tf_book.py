import json
import os
import pprint
import random

SAMPLE = []
JSON = 'tf_book.json'
CURRENT_PATH = os.getcwd()
JSON_PATH = os.path.join(CURRENT_PATH, JSON)
MENU_MESSAGE = """ 
|Show all contacts          | (enter 1)
|Add a contact              | (enter 2)
|Update a contact           | (enter 3)
|Search by city             | (enter 4)
|Search by state            | (enter 5)
|Search by name             | (enter 6)
|Search by surname          | (enter 7)
|Search by fullname         | (enter 8)
|Search by telephone number | (enter 9)
|Exit from programme        | (enter q)"""


def show_all():
    if status_json():
        return read_json()


def status_json():
    return os.path.exists(JSON_PATH)


def create_json():
    with open(JSON, 'w') as tf_book:
        json.dump(SAMPLE, tf_book)


def read_json():
    if status_json():
        with open(JSON, 'r') as json_read:
            data = json_read.read()
            data = json.loads(data)
            return data
    else:
        create_json()
        return read_json()


def check_contact(number):
    data = read_json()
    for i in data:
        if i['number'] == number:
            return True
    return False


def search_by(param, what):
    searched = []
    for i in read_json():
        if param == i[f'{what}']:
            searched.append(i)
    if len(searched) > 0:
        return searched
    else:
        return 'Not found'


def ask_info():
    name = input('Введите имя')
    surname = input('Введите фамилию')
    city = input('Введите город')
    state = input('Введите область')
    number = input('Введите номер в формате +380123456789')
    return [name, surname, number, city, state]


def ask_search(question):
    answer = input(f'{question}')
    return answer


def update_contact(name, surname, number, city, state):
    if status_json():
        if check_contact(number):
            temp_dict = {}
            entry = {
                'fullname': f'{surname} {name}',
                'name': name,
                'surname': surname,
                'number': number,
                'city': city,
                'state': state
            }
            data = read_json()
            for i in search_by(number, 'number'):
                temp_dict.update(i)
            data.remove(temp_dict)
            with open(JSON, 'w') as json_add:
                data.append(entry)
                json.dump(data, json_add, indent=4)
        else:
            print('Такого контакта нет, чтобы его добавить нажмите 2')
    else:
        create_json()
        update_contact(name, surname, number, city, state)


def add_contact(name, surname, number, city, state):
    if status_json():
        entry = {
            'fullname': f'{surname} {name}',
            'name': name,
            'surname': surname,
            'number': number,
            'city': city,
            'state': state
        }
        data = read_json()
        if check_contact(number):
            print('This number is already added, to update it enter 3')
        else:
            with open(JSON, 'w') as json_add:
                data.append(entry)
                json.dump(data, json_add, indent=4)

    else:
        create_json()
        add_contact(name, surname, number, city, state)


if __name__ == '__main__':

    ans = input(f'{MENU_MESSAGE}').lower()
    while ans != 'q':
        if ans == '1':
            pprint.pprint(show_all())
        elif ans == '2':
            add_contact(*ask_info())
        elif ans == '3':
            update_contact(*ask_info())
        elif ans == '4':
            pprint.pprint(search_by(ask_search('Enter a city'), 'city'))
        elif ans == '5':
            pprint.pprint(search_by(ask_search('Enter a state'), 'state'))
        elif ans == '6':
            pprint.pprint(search_by(ask_search('Enter a name'), 'name'))
        elif ans == '7':
            pprint.pprint(search_by(ask_search('Enter a surname'), 'surname'))
        elif ans == '8':
            pprint.pprint(search_by(ask_search('Enter a fullname(Surname Name)'), 'fullname'))
        elif ans == '9':
            pprint.pprint(search_by(ask_search('Enter a number'), 'number'))
        elif ans == 'q':
            break
        ans = input(f'{MENU_MESSAGE}').lower()
