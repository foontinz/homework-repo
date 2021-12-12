# Создайте класс Friend для хранения имени name и телефона phone. Обратите внимание, у друга может не быть телефона.
class Friend:
    def __init__(self, name, number=""):
        self.name = name
        self.phone = number


if __name__ == '__main__':
    u1 = Friend("Андрей", "+380331233333")
    u2 = Friend("Петр")

    print(u1.name)
    print(hasattr(u1, "name"))
    print(hasattr(u1, "phone"))
    print(u1.name == "Андрей")
    print(u2.name == "Петр")
    print(u1.phone == "+380331233333")
    print(u2.phone == "")
