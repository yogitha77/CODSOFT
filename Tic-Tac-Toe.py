import random
import time

class TicTacToe:
    def __init__(self):
        self.tictactoeboard = [' '] * 9
        self.present_winner = None

    def print_tictactoeboard(self):
        for row in [self.tictactoeboard[x * 3:(x + 1) * 3] for x in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_tictactoeboard_nums():
        TicTacToe_tictactoeboard = [[str(x) for x in range(y * 3, (y + 1) * 3)] for y in range(3)]
        for row in TicTacToe_tictactoeboard:
            print('| ' + ' | '.join(row) + ' |')

    def available_steps(self):
        return [x for x, spot in enumerate(self.tictactoeboard) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.tictactoeboard

    def num_empty_squares(self):
        return self.tictactoeboard.count(' ')

    def make_move(self, square, alphabet):
        if self.tictactoeboard[square] == ' ':
            self.tictactoeboard[square] = alphabet
            if self.winner(square, alphabet):
                self.present_winner = alphabet
            return True
        return False

    def winner(self, square, alphabet):
        # Visit the row
        row_ind = square // 3
        row = self.tictactoeboard[row_ind*3:(row_ind+1)*3]
        if all([spot == alphabet for spot in row]):
            return True
        # Visit the columns
        col_ind = square % 3
        column = [self.tictactoeboard[col_ind+x*3] for x in range(3)]
        if all([spot == alphabet for spot in column]):
            return True
        # Visit the diagonal
        if square % 2 == 0:
            diagonal1 = [self.tictactoeboard[x] for x in [0, 4, 8]]
            if all([spot == alphabet for spot in diagonal1]):
                return True
            diagonal2 = [self.tictactoeboard[x] for x in [2, 4, 6]]
            if all([spot == alphabet for spot in diagonal2]):
                return True
        return False

class HumanPlayer:
    def get_steps(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input('Your turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class AIPlayer:
    def get_steps(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # choose a random move
        else:
            square = self.minimax(game, 'A')['position']
        return square

    def minimax(self, state, player):
        max_player = 'A'  # AI player
        other_player = 'B' if player == 'A' else 'A'

        if state.present_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        else:
            if player == max_player:
                best = {'position': None, 'score': -float('inf')}
            else:
                best = {'position': None, 'score': float('inf')}

            for possible_steps in state.available_moves():
                state.make_steps(possible_move, player)
                sim_score = self.minimax(state, other_player)

                state.tictactoeboard[possible_move] = ' '  # undo step
                state.present_winner = None
                sim_score['position'] = possible_move

                if player == max_player:
                    if sim_score['score'] > best['score']:
                        best = sim_score
                else:
                    if sim_score['score'] < best['score']:
                        best = sim_score

            return best

def play(game, b_player, a_player, print_game=True):
    if print_game:
        game.print_tictactoeboard_nums()

    alphabet = 'B'
    while game.empty_squares():
        if alphabet == 'A':
            square = a_player.get_steps(game)
        else:
            square = b_player.get_steps(game)

        if game.make_steps(square, alphabet):
            if print_game:
                print(alphabet + f' makes a step to square {square}')
                game.print_tictactoeboard()
                print('')  # empty line

            if game.present_winner:
                if print_game:
                    print(alphabet + ' wins!')
                return alphabet  # ends the loop and exits the game
            alphabet = 'A' if alphabet == 'B' else 'B'  # change player

        # take a small break to make it easier to read it
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'was a tie')

if __name__ == '__main__':
    b_player = HumanPlayer()
    a_player = AIPlayer()
    t = TicTacToe()
    play(t, b_player, a_player, print_game=True)