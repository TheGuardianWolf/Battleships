from board_marker import BoardMarker


class Ship(object):
    def __init__(self, name, length, symbol):
        self.length = length
        self.name = name
        self.markers = [BoardMarker(symbol, False) for m in range(length)]

    def is_sunk(self):
        hits = [marker.is_hit for marker in self.markers]

        return hits.count(True) == self.length
