class Board:
    boardLength = 6
    p1StartIdx = 0
    p1EndIdx = boardLength - 1
    p2StartIdx = boardLength + 1
    p2EndIdx = boardLength * 2

    def __init__(self, player1, player2):
        # [p1 stones][p1 store][p2 stones][p2 store][curr player]
        self.state = '3x' * self.boardLength + '0x' + '3x' * self.boardLength + '0x' + '1'

    def printBoard(self, state):
        stateList = state.split('x')
        boardString = ("|{:6}".format('') + "|{:^4}" * self.boardLength
                       + "|{:6}|".format('')).format(*stateList[self.p2EndIdx:self.p2StartIdx-1:-1]) + '\n'
        dividerString = '*' * len(boardString)
        boardString += "|{:^6}".format(stateList[self.p2EndIdx+1]) + "|{:4}".format('') * self.boardLength \
                       + "|{:^6}|".format(stateList[self.p1EndIdx+1]) + '\n'
        boardString += ("|{:6}".format('') + "|{:^4}" * self.boardLength
                        + "|{:6}|".format('')).format(*stateList[0:self.p1EndIdx+1])
        print(boardString + '\n' + dividerString)

    def isTerminatedState(self, state):
        stateList = state.split('x')
        return all(x == '0' for x in stateList[self.p1StartIdx:self.p1EndIdx+1]) \
            or all(x == '0' for x in stateList[self.p2StartIdx:self.p2EndIdx+1])

    def getLegalMoves(self, state):
        stateList = state.split('x')
        stateList = [int(x) for x in stateList]
        player = stateList[-1]
        if player == 1:
            return [i+1 for i, e in enumerate(stateList[self.p1StartIdx:self.p1EndIdx+1]) if e != 0]
        else:
            return [i+1 for i, e in enumerate(stateList[self.p2StartIdx:self.p2EndIdx+1]) if e != 0]

    def getNextState(self, state, action):
        # Action 1 - 6
        stateList = state.split('x')
        stateList = [int(x) for x in stateList]
        player = stateList[-1]
        currPit = action + self.boardLength if player == 2 else action - 1
        numStonesTaken = stateList[currPit]
        stateList[currPit] = 0
        while numStonesTaken != 0:
            currPit = (currPit + 1) % (self.boardLength * 2 + 2)
            if not (player == 1 and currPit == self.p2EndIdx+1) and not (player == 2 and currPit == self.p1EndIdx+1):
                stateList[currPit] += 1
                numStonesTaken -= 1

        # landed in own empty pit, capture on both sides
        if player == 1 and currPit in range(self.p1StartIdx, self.p1EndIdx+1) and stateList[currPit] == 1 \
                and stateList[self.boardLength * 2 - currPit] != 0:
            stateList[self.p1EndIdx+1] += stateList[currPit] + stateList[self.boardLength * 2 - currPit]
            stateList[currPit] = 0
            stateList[self.boardLength * 2 - currPit] = 0
        elif player == 2 and currPit in range(self.p2StartIdx, self.p2EndIdx+1) and stateList[currPit] == 1 \
                and stateList[self.boardLength * 2 - currPit] != 0:
            stateList[self.p2EndIdx+1] += stateList[currPit] + stateList[self.boardLength * 2 - currPit]
            stateList[currPit] = 0
            stateList[self.boardLength * 2 - currPit] = 0

        currState = 'x'.join([str(x) for x in stateList])
        if self.isTerminatedState(currState):
            stateList[self.p1EndIdx+1] += sum(stateList[self.p1StartIdx:self.p1EndIdx+1])
            stateList[self.p2EndIdx+1] += sum(stateList[self.p2StartIdx:self.p2EndIdx+1])
            for i in range(self.boardLength):
                stateList[i], stateList[i+self.p2StartIdx] = 0, 0
        else:
            # didnt land in store, switch turns
            if player == 1 and currPit != self.p1EndIdx + 1:
                stateList[-1] = 2
            elif player == 2 and currPit != self.p2EndIdx + 1:
                stateList[-1] = 1
        return 'x'.join([str(x) for x in stateList])
