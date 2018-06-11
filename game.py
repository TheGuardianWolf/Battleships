from player import Player
from adapter_cli import AdapterCLI
from adapter_ai import AdapterAI
from board import Board


class Game(object):
    def __init__(self, board_size):
        self.player_turn = 0
        self.board_size = board_size

        ship_types = [('Aircraft Carrier', 5, 'A'), ('Submarine', 4, 'S'),
                      ('Destroyer', 3, 'D'), ('Patrol Boat', 3, 'P')]

        self.players = [
            Player('Human',
                   AdapterCLI(),
                   Board(board_size), Board(board_size), ship_types),
            Player('AI',
                   AdapterAI(board_size),
                   Board(board_size), Board(board_size), ship_types)
        ]

    def run(self):
        print('Beginning setup phase...')
        for i, player in enumerate(self.players):
            print('Player', i, 'setup...')
            player.setup()

        print('Beginning main phase...')
        while (not self.game_over()):
            print('Player {}\'s turn'.format(str(self.player_turn)))
            self.players[self.player_turn].print_target_board()

            if self.players[self.player_turn].strike(self.players[(
                    self.player_turn + 1) % len(self.players)]) is True:
                print('Hit!')
            else:
                print('Miss!')
                self.player_turn = (
                    self.player_turn + 1) % len(self.player_turn)

    def game_over(self):
        for i, player in enumerate(self.players):
            if player.is_defeated() is True:
                print('Game over! Player {} lost!'.format(i))


if __name__ == "__main__":
    game = Game(10)
    game.run()
