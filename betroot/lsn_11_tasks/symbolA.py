###Задача Напишите класс который будет "рисовать" букву псевдографикой. Например чтобы диезами написать букву A нам нужно напечатать
class SymbolA:
    def __init__(self, symbol='#'):
        self.smb = symbol
        self.drawing = (f' {self.smb * 3}\n{self.smb}  {self.smb}\n{self.smb * 4}\n{self.smb}  {self.smb}')
        self.iteration = 0

    def draw(self):
        print(self.drawing)

    def line(self, index):
        temp_line = self.drawing.split('\n')
        print(temp_line[index - 1])

    def itline(self):
        temp_line = self.drawing.split('\n')
        try:
            print(temp_line[self.iteration])
            self.iteration += 1
        except IndexError:
            raise StopIteration('Куда еще')

if __name__ == '__main__':

    a = SymbolA("l")
    a.itline()
    a.itline()

