class Alo:
    def __init__(self):
        self.a = 123


    @property
    def a(self):
        return self.a

    @a.setter
    def a(self, num):
        self.a = num