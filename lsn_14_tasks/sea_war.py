import pprint
from random import choice
from random import randint


class Board:
    SIZE = 10
    FREE = 69
    HEALTH_SHIP = 99

    def __init__(self):
        self.ships = []
        self.board = {}
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.board[(i, j)] = self.FREE

    def check_in_border(self, coords: tuple):
        return coords in self.board

    def _choose_coords(self):
        return choice(list(self.board.keys()))

    def _choose_direction(self):
        return choice([1, 2])

    def check_coords(self, coords: tuple):
        if self.check_in_border(coords):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        temp_coords = (coords[0] + i, coords[1] + j)
                        if self.board[temp_coords] != self.FREE:
                            return False
                    except (IndexError, KeyError):
                        pass
            return True
        return self.check_in_border(coords)

    def build_ship(self, size):
        while True:
            temp_dir = self._choose_direction()
            temp_coords = self._choose_coords()

            if temp_dir == 1:
                temp_coord_listx = [(temp_coords[0] + x, temp_coords[1]) for x in range(0, size)]
                if not all([self.check_coords(x) for x in temp_coord_listx]):
                    continue
            elif temp_dir == 2:
                temp_coord_listy = [(temp_coords[0], temp_coords[1] + y) for y in range(0, size)]
                if not all([self.check_coords(y) for y in temp_coord_listy]):
                    continue

            for x in range(0, size):
                if temp_dir == 1:
                    self.board.update({(temp_coords[0] + x, temp_coords[1]): self.HEALTH_SHIP})
                elif temp_dir == 2:
                    self.board.update({(temp_coords[0], temp_coords[1] + x): self.HEALTH_SHIP})

            a = Ship(size, temp_dir, temp_coords, self)
            break
        return a

    def display_board(self):
        for j in range(self.SIZE):
            print()
            for i in range(self.SIZE):
                if self.board[(i, j)] == self.FREE:
                    print('#', end=' ')
                else:
                    print('@', end=' ')

    def build_ships(self):
        board.build_ship(4)
        board.build_ship(3)
        board.build_ship(3)
        board.build_ship(2)
        board.build_ship(2)
        board.build_ship(2)
        board.build_ship(1)
        board.build_ship(1)
        board.build_ship(1)
        board.build_ship(1)

    @property
    def get_ships(self):
        return self.ships

    @get_ships.setter
    def set_ships(self, ships: list):
        self.ships = ships


class Ship:
    # 1 - horizontal
    # 2 - vertical
    def __init__(self, size: int, direction: int, coords: tuple, board: Board):
        if isinstance(board, Board):
            self.board = board
            self._ship_update()
        else:
            raise TypeError('Board for ship is not board 0_o')
        self.size = size
        self.direction = direction
        self.coords = coords

    def _ship_update(self):
        temp_list = self.board.get_ships
        temp_list.append(self)
        self.board.set_ships = temp_list

    def __repr__(self):
        return f'{self.size} палубник {self.direction} направления , по координатам {self.coords[0] + 1, self.coords[1] + 1}'


board = Board()
board.build_ships()
board.display_board()
print()
for ship in board.get_ships:
    print(ship)
exit()
