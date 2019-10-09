"""
Tic-tac-toe heuristic

Estimates the value of the board
It checks rows, columns and diagonals for local patterns corresponding 
to different configurations of X, O and _

@author: milos
"""


class Heuristics:
    """
    This is an example of a basic heuristic class.

    Feel free to modify or extend this class. The minimum
    requirement is to implement the 'eval_board' function with
    the same method declaration as shown below.
    """
    def __init__(self):
        """
        'patterns' are possible features indicating winning.
        'i' means it is 'my' marker;
        't' means it is 'the other' marker.
        For example, if my marker is 'X', then 'i'='X' and 't'='O'.
        """
        self.patterns = {'iiiii': 100,
                         '_iiii_': 50,
                         '_iii_': 10,
                         '_i_ii_': 10,
                         '_ii__': 2,
                         '__ii_': 2,
                         '__i__': 1,
                         'ittt_': 1
                         }

    def eval_board(self, board, this_player):
        """
        Evaluate the board standing in 'this_player' position

        :param board:
        :param this_player: either 'X' or 'O'
        :return: the winning score for 'this_player'
        """
        that_player = 'X' if this_player == 'O' else 'O'
        return self.eval_player(board, this_player) \
                - self.eval_player(board, that_player)

    def eval_player(self, board, player):
        """
        It checks rows, columns, diagonal and counter diagonal for local patterns.
        """
        def _eval_row(board, player):
            score = 0
            for row in board:
                _str = ''.join([_change_char(c, player) for c in row])
                score += _eval_str(_str, self.patterns)
            return score

        def _eval_col(board, player):
            score = 0
            n = len(board)
            for j in range(n):
                _str = ''.join([_change_char(board[i][j], player) for i in range(n)])
                score += _eval_str(_str, self.patterns)
            return score

        def _eval_diag(board, player):
            score = 0
            n = len(board)
            for diff in range(1-n, n):
                buff = list()
                for i in range(n):
                    j = i + diff
                    if 0 <= j < n:
                        buff.append(_change_char(board[i][j], player))
                _str = ''.join(buff)
                score += _eval_str(_str, self.patterns)
            return score

        def _eval_counter_diag(board, player):
            score = 0
            n = len(board)
            for _sum in range(2*n-1):
                buff = list()
                for i in range(n):
                    j = _sum - i
                    if 0 <= j < n:
                        buff.append(_change_char(board[i][j], player))
                _str = ''.join(buff)
                score += _eval_str(_str, self.patterns)
            return score

        def _change_char(c, player):
            that_player = 'X' if player == 'O' else 'O'
            if c == player:
                return 'i'
            elif c == that_player:
                return 't'
            else:
                return '_'

        def _eval_str(_str, patterns):
            score = 0
            for pat in patterns.items():
                if pat[0] in _str:
                    score += pat[1]
            return score

        return sum((_eval_row(board, player),
                   _eval_col(board, player),
                   _eval_diag(board, player),
                   _eval_counter_diag(board, player)))
