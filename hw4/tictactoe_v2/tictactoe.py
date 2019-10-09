"""
Tic-tac-toe on kxk board (default)
@author: milos
"""


class TicTacToe:
    """
    This is playing TicTacToe game.

    Player X makes the first move.
    Note: you do NOT have to modify this class.
    """
    WINS = 'Player {}({}) wins!'
    TIED = 'It is a tie!'
    MIN_NUM = 5

    def __init__(self, board_size, playerX, playerO, print_steps):
        """
        Initialization of one game.

        :param board_size: k*k
        :param playerX: makes the first move
        :param playerO: makes the second move
        :param print_steps: if True, print the intermediate steps
        """
        if board_size < TicTacToe.MIN_NUM:
            raise ValueError('The board size must be >= {}'.format(TicTacToe.MIN_NUM))
        self.board_size = board_size
        self.board = [['_'] * self.board_size for i in range(self.board_size)]
        self.num_moves = 0
        self.playerX = playerX.set_marker('X')
        self.playerO = playerO.set_marker('O')
        self.print_steps = print_steps

    def reset(self):
        """
        Reset the game. All cells are empty, marked as '_'.
        """
        for i, row in enumerate(self.board):
            for j, c in enumerate(row):
                row[j] = '_'
        self.num_moves = 0

    def set_players(self, playerX, playerO):
        """
        Set the two players. X moves the first.
        """
        self.playerX = playerX.set_marker('X')
        self.playerO = playerO.set_marker('O')

    def start(self):
        """
        Starts to play the game.

        :return: the end result
        """
        def _make_one_move(game, player):
            num_empty_cells = game.board_size**2 - game.num_moves
            i, j = player.make_one_move(game.board, num_empty_cells)
            game.num_moves += 1
            if game.print_steps:
                print('{}({}) makes one move at ({}, {})'.format(player.name, player.marker, i, j))
                game.print_board()
                a=input('press Return')
            else:
                print(player.marker, end='', flush=True)
            return game.check_end(i, j)

        def _result(end_flag, player):
            if end_flag == TicTacToe.TIED:
                return end_flag, None
            else:
                return end_flag.format(player.name, player.marker), player

        print('Starting a new game! Board size = {}'.format(self.board_size))
        print('Player {} vs. Player {}'.format(self.playerX.name, self.playerO.name))
        print("{} makes the first move with 'X'".format(self.playerX.name))
        while True:
            # Player X makes one move
            end_flag = _make_one_move(self, self.playerX)
            if end_flag is not None:
                print()
                return _result(end_flag, self.playerX)

            # Player O makes one move
            end_flag = _make_one_move(self, self.playerO)
            if end_flag is not None:
                print()
                return _result(end_flag, self.playerO)

    def print_board(self):
        for row in self.board:
            a=''
            for i in row:
                a+=i
            print(a)

    def check_end(self, i, j):
        """
        Check if the games ends after board[i][j] is filled.
        """
        def _check_row(i, j, board):
            a, b = j, j
            while a > 0 and board[i][a-1] == board[i][j]:
                a -= 1
            while b < len(board)-1 and board[i][b+1] == board[i][j]:
                b += 1
            return (b-a+1) >= TicTacToe.MIN_NUM

        def _check_col(i, j, board):
            a, b = i, i
            while a > 0 and board[a-1][j] == board[i][j]:
                a -= 1
            while b < len(board)-1 and board[b+1][j] == board[i][j]:
                b += 1
            return (b-a+1) >= TicTacToe.MIN_NUM

        def _check_diag(i, j, board):
            a, b = i, i
            while a > 0 and (j+a-i) > 0 and board[a-1][j+a-i-1] == board[i][j]:
                a -= 1
            while b < len(board)-1 and (b-i+j) < len(board)-1 and board[b+1][b-i+j+1] == board[i][j]:
                b += 1
            return (b-a+1) >= TicTacToe.MIN_NUM

        def _check_counter_diag(i, j, board):
            a, b = i, i
            while a > 0 and (i+j-a) < len(board)-1 and board[a-1][i+j-a+1] == board[i][j]:
                a -= 1
            while b < len(board)-1 and (i+j-b) > 0 and board[b+1][i+j-b-1] == board[i][j]:
                b += 1
            return (b-a+1) >= TicTacToe.MIN_NUM

        if _check_row(i, j, self.board) or \
                _check_col(i, j, self.board) or \
                _check_diag(i, j, self.board) or \
                _check_counter_diag(i, j, self.board):
            return TicTacToe.WINS
        elif self.num_moves == self.board_size ** 2:
            return TicTacToe.TIED
        else:
            return None
