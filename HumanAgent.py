class HumanAgent:
    name = None

    def __init__(self, name='Human'):
        self.name = name

    def getAction(self, board):
        actions = board.getLegalMoves(board.state)
        print("Available actions: {}".format(actions))
        action = 0
        while action not in actions:
            action = input('Please choose an action: ')
            action = int(action)
        return action
