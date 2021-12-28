import random


class Board:
    FREE = '#'

    def __init__(self, width, length):
        self.length = width
        self.witdth = length

        self._initialize_board()

    def _initialize_board(self):
        self.board_values = {}
        for x in range(1, self.witdth + 1):
            for y in range(1, self.length + 1):
                self.board_values.update({(x, y): self.FREE})

    def place(self, *args):
        for data in args:
            self.board_values.update({(data[1], data[2]): data[0]})

    def place_random(self, symb, amount):
        for i in range(amount):
            temp_holder = random.choice(list(self.board_values.keys()))
            self.board_values.update({temp_holder: symb})

    def __str__(self):

        result = ''
        for y in range(1, self.length + 1):
            for x in range(1, self.witdth + 1):
                result += self.board_values[(x, y)] + '  '
            result += '\n'
        print()
        return result


tic_tac_toe = Board(3, 3)
chess = Board(8, 8)
minesweeper = Board(30, 16)
tic_tac_toe.place(('X', 1, 1))
chess.place(('wK', 4, 0), *(('wP', i, 1) for i in range(8)))
minesweeper.place_random('*', 99)
print(chess, tic_tac_toe, minesweeper)
