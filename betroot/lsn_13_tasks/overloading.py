class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('meeee')


class Dog(Animal):
    def talk(self):
        print('woof')


class Cat(Animal):
    def talk(self):
        print('meow')

def speak(animal:Animal):
    animal.talk()
