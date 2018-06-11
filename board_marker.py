class BoardMarker(object):
    def __init__(self, symbol, empty):
        self.is_hit = False
        self.symbol = symbol
        self.empty = empty

    def get_symbol(self):
        return self.symbol if self.is_hit is False else 'X'
