from Board import Board
from RandomAgent import RandomAgent
from HumanAgent import HumanAgent
from MinimaxAgent import MinimaxAgent

if __name__ == '__main__':
    p1 = MinimaxAgent(1, 12, 'komputabb1')
    p2 = MinimaxAgent(2, 12, 'komputabb2')
    b = Board(p1, p2)
    b.printBoard(b.state)
    while not b.isTerminatedState(b.state):
        currentPlayer = int(b.state.split('x')[-1])
        currentPlayerName = ''
        if currentPlayer == 1:
            currentPlayerName = p1.name
            nextAction = p1.getAction(b)
        else:
            currentPlayerName = p2.name
            nextAction = p2.getAction(b)
        print("Player {} selected pit {}. ".format(currentPlayerName, nextAction))
        b.state = b.getNextState(b.state, nextAction)
        b.printBoard(b.state)
    stateList = b.state.split('x')
    print("Game terminated. Player 1 final score: {}. Player 2 final score: {}.".format(stateList[b.p1EndIdx+1],
                                                                                        stateList[b.p2EndIdx+1]))
