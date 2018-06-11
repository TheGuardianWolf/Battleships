from adapter import Adapter
from random import randint


class AdapterAI(Adapter):
    def __init__(self, board_size):
        self.board_size = board_size

    def get_grid(self, prompt):
        move = randint(0, self.board_size - 1)
        print(prompt + ':', move)
        return move

    def get_bool(self, prompt):
        move = randint(0, 1) > 0
        print(prompt + ':', move)
        return move
