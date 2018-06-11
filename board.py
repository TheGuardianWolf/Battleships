from board_marker import BoardMarker


class Board(object):
    def __init__(self, size):
        self.size = size
        self.clear()

    def is_empty(self, x, y):
        return self.grid[y][x].empty

    def mark_hit(self, x, y):
        if x < 0 or y < 0:
            raise IndexError('Position not in grid')

        if (self.grid[y][x].is_hit is True):
            return False
        else:
            self.grid[y][x].is_hit = True
            return True

    def place_ship(self, ship, x, y, vertical):
        if (vertical is True and y + ship.length > self.size) or (
                vertical is False
                and x + ship.length > self.size) or x < 0 or y < 0:
            raise IndexError('Position not in grid')

        for i in range(len(ship.markers)):
            if (vertical is True and self.grid[y + i][x].empty is False) or (
                    vertical is False and self.grid[y][x + i].empty is False):
                raise ValueError('Specified position is not empty')

        for i, marker in enumerate(ship.markers):
            if vertical is True:
                self.grid[y + i][x] = marker
            else:
                self.grid[y][x + i] = marker

        return True

    def print(self):
        print('  ', * [' {} '.format(i) for i in range(self.size)])
        print(
            * [
                ' {} '.format(i) + '[' + '] ['.join(
                    [marker.symbol for marker in row]) + ']'
                for i, row in enumerate(self.grid)
            ],
            sep='\n')

    def clear(self):
        self.grid = [[BoardMarker(" ", True) for x in range(self.size)]
                     for y in range(self.size)]
