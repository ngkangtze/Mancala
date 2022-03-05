import random


class RandomAgent:
    name = None

    def __init__(self, name='RandomBot'):
        self.name = name

    def getAction(self, board):
        actions = board.getLegalMoves(board.state)
        action = random.choice(actions)
        print("I am {}! I choose {}!".format(self.name, action))
        return action
