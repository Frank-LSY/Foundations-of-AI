"""
Let's play the tic-tac-toe game!

@author: milos
"""
from tictactoe import TicTacToe
from player import Player
from heuristics import Heuristics
from naive_heuristics import NaiveHeuristics

# define heuristics
basic_h = Heuristics()
naive_h = NaiveHeuristics()

#define players
playerA = Player(1, basic_h, 'Player A')
playerB = Player(1, naive_h, 'Player B')
stats = {'Player A wins': 0, 'Player B wins': 0, 'Tied': 0}

# set the board size of the game
board_size=10

# set the ply search for the player
k=2
print('Players using K-ply =', k)
playerA.set_k_ply(k)
playerB.set_k_ply(k)


# start the game with players A and B
# use print_steps=False to remove printouts of moves
game = TicTacToe(board_size, playerA, playerB, print_steps=True)

for i in range(5):
    # Player A moves first
    game.reset()
    game.set_players(playerA, playerB)
    result, winner = game.start()
    print(result)
    if winner is None:
        stats['Tied'] += 1
    else:
        stats['{} wins'.format(winner.name)] += 1

    # Player B moves first
    game.reset()
    game.set_players(playerB, playerA)
    result, winner = game.start()
    print(result)
    if winner is None:
        stats['Tied'] += 1
    else:
        stats['{} wins'.format(winner.name)] += 1

print(stats)
