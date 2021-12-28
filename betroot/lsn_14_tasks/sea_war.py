import time
from random import choice
from random import randint


class War:
    FREE = 69
    HEALTH_SHIP = 99
    DEFEATED_SHIP = 88
    MISSED = 11

    def __init__(self, opponent1: 'Board', opponent2: 'Board'):

        if isinstance(opponent1, Board) and isinstance(opponent2, Board):
            self.bot1 = opponent1
            self.bot2 = opponent2
        else:
            raise TypeError('Players has wrong type')

    def shoot(self, player: int):
        shoot_holder = (randint(0, 9), randint(0, 9))
        if player == 1:
            if shoot_holder in self.bot1.get_shooted:
                return self.shoot(player)
            self.bot1.get_shooted.append(shoot_holder)
            if self.bot2.get_board[shoot_holder] == self.FREE:
                self.bot1.enemy_board.update({shoot_holder: self.MISSED})
                return
            if self.bot2.get_board[shoot_holder] == self.HEALTH_SHIP:
                self.bot2.get_board.update({shoot_holder: self.DEFEATED_SHIP})
                self.bot1.get_enemy_board.update({shoot_holder: self.DEFEATED_SHIP})
                for ship in self.bot2.get_ships:
                    if shoot_holder in ship.get_total_coords:
                        ship.get_total_coords.update({shoot_holder: False})
                        if ship.check_life():
                            self.bot2.get_ships.remove(ship)
        elif player == 2:
            if shoot_holder in self.bot2.get_shooted:
                return self.shoot(player)
            self.bot2.get_shooted.append(shoot_holder)
            if self.bot1.get_board[shoot_holder] == self.FREE:
                self.bot2.enemy_board.update({shoot_holder: self.MISSED})
                return
            if self.bot1.get_board[shoot_holder] == self.HEALTH_SHIP:
                self.bot1.get_board.update({shoot_holder: self.DEFEATED_SHIP})
                self.bot2.get_enemy_board.update({shoot_holder: self.DEFEATED_SHIP})
                for ship in self.bot1.get_ships:
                    if shoot_holder in ship.get_total_coords:
                        ship.get_total_coords.update({shoot_holder: False})
                        if ship.check_life():
                            self.bot1.get_ships.remove(ship)

    def war_finish(self):

        if self.bot1.is_over():
            print('Bot #2 won. Humanity in danger')
            time.sleep(10)
            exit()
        elif self.bot2.is_over():
            print('Bot #1 won. Humanity in danger ')
            time.sleep(10)
            exit()

    def war_begin(self):
        print('''
        Чужая тетрадь:
        ⚪ - не тронута
        ⚫ - ударил но не попал
        ⦻ - попал
        Своя тетрадь:
        ⚪ - пустая
        ⚫ - кораблик
        ⦻ - попали
        ''')
        print('-' * 100)
        print('Бот №1 тетрадочка        \t\t\t    Бот №2 тетрадочка')
        self.bot1.display_board()
        print('Бот №2 тетрадочка          \t\t\t  Бот №1 тетрадочка')
        self.bot2.display_board()
        print('-' * 100)
        time.sleep(2)
        self.war_loop()


    def war_loop(self):
        self.shoot(1)
        self.shoot(2)
        print('Бот №1 тетрадочка            \t\t\tБот №2 тетрадочка')
        self.bot1.display_board()
        print('Бот №2 тетрадочка            \t\t\tБот №1 тетрадочка')
        self.bot2.display_board()
        print('-' * 100)
        self.war_finish()
        time.sleep(2)
        self.war_loop()


class Board:
    SIZE = 10
    FREE = 69
    HEALTH_SHIP = 99
    DEFEATED_SHIP = 88
    MISSED = 11

    def __init__(self):
        self.ships = []
        self.board = {}
        self.enemy_board = {}
        self.shooted_places = []

        self.generate_board()
        self.generate_enemy_board()
        self.build_ships()

    def is_over(self):
        return len(self.ships) == 0

    def generate_board(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.board[(i, j)] = self.FREE

    def generate_enemy_board(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.enemy_board[(i, j)] = self.FREE

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
        temp_list = [' ', '𝟎', '①', '𝟐', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨']
        [print(k, end='  ') for k in temp_list]
        print('', end='    ')
        [print(k, end='  ') for k in temp_list]

        for j in range(self.SIZE):
            print()
            print(j, end='  ')
            for i in range(self.SIZE):

                if self.board[(i, j)] == self.FREE:
                    print('⃝⚪', end='  ')
                elif self.board[(i, j)] == self.HEALTH_SHIP:
                    print('⚫', end='  ')
                elif self.board[(i, j)] == self.DEFEATED_SHIP:
                    print('⦻', end='  ')

            print('\t', end='')

            print(j, end='  ')
            for i in range(self.SIZE):
                if self.enemy_board[(i, j)] == self.FREE:
                    print('⃝⚪', end='  ')
                elif self.enemy_board[(i, j)] == self.MISSED:
                    print('⚫', end='  ')
                elif self.enemy_board[(i, j)] == self.DEFEATED_SHIP:
                    print('⦻', end='  ')
        print()

    def build_ships(self):
        self.build_ship(4)
        self.build_ship(3)
        self.build_ship(3)
        self.build_ship(2)
        self.build_ship(2)
        self.build_ship(2)
        self.build_ship(1)
        self.build_ship(1)
        self.build_ship(1)
        self.build_ship(1)

    @property
    def get_shooted(self):
        return self.shooted_places

    @property
    def get_board(self):
        return self.board

    @property
    def get_ships(self):
        return self.ships

    @property
    def get_enemy_board(self):
        return self.enemy_board


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
        self.start_coords = coords
        self.total_coords = {}

        self._declare_total_coords()

    def _declare_total_coords(self):
        for i in range(self.size):
            if self.direction == 1:
                self.total_coords.update({(self.start_coords[0] + i, self.start_coords[1]): True})
            elif self.direction == 2:
                self.total_coords.update({(self.start_coords[0], self.start_coords[1] + i): True})

    def _ship_update(self):
        self.board.get_ships.append(self)

    def check_life(self):
        if not any(list(self.total_coords.values())):
            return True
        return False

    @property
    def get_total_coords(self):
        return self.total_coords


board = Board()
board2 = Board()
war = War(board, board2)
war.war_begin()
exit()
