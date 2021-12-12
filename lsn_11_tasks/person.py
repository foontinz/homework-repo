class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.name} {self.surname} and I’m {self.age} years old')


a = Person('lo ', 'ov', 12)
a.talk()
