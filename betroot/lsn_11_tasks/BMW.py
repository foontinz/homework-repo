import pprint


class BMW:
    logo = 'BMW'

    def __init__(self, number, color='black'):
        self.number = number
        self.color = color

    def info(self):
        pprint.pprint({'logo': self.logo,
                       'number': self.number,
                       'color': self.color})

#ассерты я немного поменял, ибо формат вывода инфо сделал через словарь(считаю так лучше выглядит)

car1 = BMW("АА1232ОО")
assert car1.color == "black"
assert car1.number == "АА1232ОО"

car2 = BMW("AA2121EE", "white")
assert car2.color == "white"
assert car2.number == "AA2121EE"

car3 = BMW("AA2121EE", "red")
assert car3.color == "red"
assert car3.number == "AA2121EE"

car3.logo = "MAZERATTI"
BMW.logo = "BMWQ+"
car1.info()
car2.info()
car3.info()