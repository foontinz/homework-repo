class Marker:
    RASHOD = 0.5
    INK = 4

    def __init__(self, string, ):
        self.string = string
        self.current_ink = self.INK

    def ink_symbols(self):
        new_string = ['[']
        temp_ink = self.current_ink
        for symbol in self.string:
            if symbol == ' ':
                new_string.append(symbol)
            else:
                if temp_ink > self.RASHOD:
                    new_string.append(symbol)
                    temp_ink -= self.RASHOD
                elif temp_ink == self.RASHOD:
                    new_string.append(symbol)
                    new_string.append(']')
                    temp_ink -= self.RASHOD
                else:
                    new_string.append(symbol)
        if temp_ink > 0:
            new_string.append(']')
        return ''.join(new_string)

    def fuel_ink(self, amount: int):
        self.current_ink += amount
        print(f'Поздравляем вы заправились на {amount}')

m = Marker('Николай, Алексей валерий Золото')
print(m.ink_symbols())
m.fuel_ink(2)
print(m.ink_symbols())
m.fuel_ink(100)
print(m.ink_symbols())
