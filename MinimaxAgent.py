class MinimaxAgent:
    def __init__(self, playerNum, depth, name='MinimaxBot'):
        self.name = name
        self.playerNum = playerNum
        self.depth = depth
        self.max = 1000
        self.min = -1000

    def getAction(self, board):
        actions = board.getLegalMoves(board.state)
        values = []
        currentActionValue = self.min-1
        currentAction = 0
        for action in actions:
            nextState = board.getNextState(board.state, action)
            value = self.minimax(self.depth, nextState, board, self.min, self.max)
            values += [value]
            if value > currentActionValue:
                currentActionValue = value
                currentAction = action
        print("Position evaluation: {}".format(max(values)))
        return currentAction

    def evaluate(self, state, board):
        stateList = state.split('x')
        p1Store = int(stateList[board.p1EndIdx + 1])
        p2Store = int(stateList[board.p2EndIdx + 1])
        score = p1Store - p2Store
        if score == 0:
            return 0
        if self.playerNum == 2:
            score = -score
        if board.isTerminatedState(state):
            return int(100 * score / abs(score))
        return score

    def minimax(self, depth, state, board, alpha, beta):
        if depth == 0 or board.isTerminatedState(state):
            return self.evaluate(state, board)
        stateList = state.split('x')
        currPlayer = int(stateList[-1])
        if currPlayer == self.playerNum:
            best = self.min
            for action in board.getLegalMoves(state):
                nextState = board.getNextState(state, action)
                stateValue = self.minimax(depth-1, nextState, board, alpha, beta)
                best = max(best, stateValue)
                alpha = max(alpha, best)
                if beta <= best:
                    break
            return best
        else:
            best = self.max
            for action in board.getLegalMoves(state):
                nextState = board.getNextState(state, action)
                stateValue = self.minimax(depth - 1, nextState, board, alpha, beta)
                best = min(best, stateValue)
                beta = min(beta, best)
                if best <= alpha:
                    break
            return best
