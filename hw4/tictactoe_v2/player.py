"""
Tic-tac-toe game player
@author: milos
"""

import random


class Player:
    """One game player

    This implementation assumes using k-ply search
    Note: you do NOT have to modify this class.
    """
    def __init__(self, k, heuristic, name):
        """
        :param k: the k-ply
        :param heuristic: some heuristic strategy
        :param name: name of the player
        """
        self.k = k
        self.heuristic = heuristic
        self.name = name
        self.marker = None

    def set_marker(self, marker):
        """
        :param marker: either 'X' or 'O'
        """
        self.marker = marker
        return self

    def set_k_ply(self, k):
        self.k = k

    def make_one_move(self, board, num_empty_cells):
        """
        Makes one move based on the current board configuration.

        In particular, apply k-ply to foresee the next k steps.
        The heuristic will evaluate the board at the last step.

        :param board: the current board
        :param num_empty_cells: how many empty cells left
        :return: (i, j), the position to make the move
        """
        def scoring(player_marker, board, heuristic, k):
            """
            A recursive implementation of the k-ply search.

            :param player_marker: 'X' or 'O'
            :param board:
            :param heuristic:
            :param k:
            :return: (1) candidate moves: [(i, j, score)]
                     (2) whether use min or max to find the best score
            """
            candidates = list()  # [(i, j, score)]
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == '_':
                        board[i][j] = player_marker
                        if k == 1:
                            score = heuristic.eval_board(board, player_marker)
                        else:
                            another_marker = 'X' if player_marker == 'O' else 'O'
                            choices, metric = scoring(another_marker, board, heuristic, k-1)
                            score = metric(choices, key=lambda t: t[2])[2]
                        candidates.append((i, j, score))
                        board[i][j] = '_'
            return candidates, min if k % 2 == 0 else max

        k = min(self.k, num_empty_cells)
        candidates, metric = scoring(self.marker, board, self.heuristic, k)
        best_score = metric(candidates, key=lambda t: t[2])[2]
        final_choices = [t[:2] for t in candidates if t[2] == best_score]
        i, j = random.choice(final_choices)
        board[i][j] = self.marker
        return i, j
