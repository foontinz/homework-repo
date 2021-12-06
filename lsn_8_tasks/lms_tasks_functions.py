# Напишите функцию которая будет переводить возраст с Земного на Марсианский. В году на Земле 365 дней а на марсе 687
def mars_to_earth(age: int):
    mars_age = (age / 365) * 687
    return mars_age


# Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
# Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"
def greet(name: str, word: str = '-'):
    return f'{name} ты сегодня {word}!'


# Напишите функцию joinA которая принимает неограниченное количество значений любого типа
# и возвращает строку где эти значения склеены через символ A
def joinA(*args):
    # сложновата
    magic = 'A'.join([str(x) if type(x) != bool else 'False' if x == False else 'True' for x in args])
    return magic


if __name__ == '__main__':
    print(joinA(False, 1, 'str'))
