from ship import Ship


class Player(object):
    def __init__(self, name, adapter, target_board, placement_board,
                 ship_types):
        self.name = name
        self.adapter = adapter
        self.target_board = target_board
        self.placement_board = placement_board
        self.ship_types = ship_types

    def setup(self):
        self.clear_board()
        self.clear_ships()
        self.place_ships()

    def clear_board(self):
        self.placement_board.clear()
        self.target_board.clear()

    def clear_ships(self):
        self.ships = []

    def is_defeated(self):
        sunk = [ship.is_sunk() for ship in self.ships]
        return sunk.count(True) == len(self.ships)

    def place_ships(self):
        self.print_placement_board()

        for name, length, symbol in self.ship_types:
            ship = Ship(name, length, symbol)
            self.ships.append(ship)

            ship_placed = False
            while (not ship_placed):
                print('Placing ship {} of length {}'.format(name, length))
                x = self.adapter.get_grid('Enter x coordinate: ')
                y = self.adapter.get_grid('Enter y coordinate: ')
                v = self.adapter.get_bool(
                    'Place vertical? (0 for False, 1 for True): ')

                try:
                    self.placement_board.place_ship(ship, x, y, v)
                    ship_placed = True
                    print('Ship placed')
                except (IndexError, ValueError) as error:
                    print('Placement error, try again')

                self.print_placement_board()

    def print_target_board(self):
        self.target_board.print()

    def print_placement_board(self):
        self.placement_board.print()

    def strike(self, player):
        while (True):
            print('Attacking enemy position')
            x = self.adapter.get_grid('Enter x coordinate: ')
            y = self.adapter.get_grid('Enter y coordinate: ')

            try:
                if self.target_board.mark_hit(x, y) is True:
                    return player.confirm_hit(x, y)
                else:
                    raise IndexError('Coordinates already hit')
            except IndexError:
                print('Coordinates invalid, try again')

    def confirm_hit(self, x, y):
        self.placement_board.mark_hit(x, y)
        return not self.placement_board.is_empty(x, y)
