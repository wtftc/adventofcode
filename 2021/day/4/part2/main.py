import collections

class BingoNumber:
    def __init__(self, row, col, marked=False):
        self.row = row
        self.col = col
        self.marked = marked

    def __repr__(self):
        return f'row: {self.row}, col: {self.col}, marked: {self.marked}'

class BingoBoard:
    def __init__(self, data):
        self.parseBoard(data)
        self.winner = False

    def parseBoard(self, data):
        self.data = data
        self.numberToPos = {}
        self.board = []
        self.rowCount = len(data)
        for row, line in enumerate(data):
            intLine = [int(x) for x in line.strip().replace('  ', ' ').split(' ')]
            self.colCount = len(intLine)
            for col, num in enumerate(intLine):
                self.numberToPos[num] = BingoNumber(row, col, marked=False)
            self.board.append(intLine)

    def mark(self, number):
        """
        Marks a number on the bingo board
        :param number: The number to mark
        :return: True if this board is a winner
        """
        if number in self.numberToPos:
            self.numberToPos[number].marked = True
            if not self.winner:
                return self.checkWinner()
        return self.winner

    def checkWinner(self):
        for row in self.board:
            rowWinner = True
            for num in row:
                if not self.numberToPos[num].marked:
                    rowWinner = False
                    break
            if rowWinner:
                self.winner = True

        for col in range(self.colCount):
            colWinner = True
            for row in range(self.rowCount):
                if not self.numberToPos[self.board[row][col]].marked:
                    colWinner = False
                    break
            if colWinner:
                self.winner = True

        return self.winner

    def winningScore(self, lastNumber):
        totalUnmarked = 0
        for row in self.board:
            for num in row:
                if not self.numberToPos[num].marked:
                    totalUnmarked += num

        return totalUnmarked * lastNumber

    def __repr__(self):
        rows = []
        for row in self.board:
            line = []
            for num in row:
                prefix = ' ' if not self.numberToPos[num].marked else '*'
                line.append(f'{prefix}{num:2}')
            rows.append(' '.join(line))
        return '\n'.join(rows)

class BoardCollection:
    def __init__(self):
        self.boards = []

    def processInput(self, input):
        self.drawOrder = [int(x) for x in input[0].split(',')]

        input = input[2:]
        #go until blank line
        curBoardData = []
        for line in input:
            if not line.strip():
                #finished board
                self.boards.append(BingoBoard(curBoardData))
                curBoardData = []
            else:
                curBoardData.append(line)

        #make sure we get the last board
        if curBoardData:
            self.boards.append(BingoBoard(curBoardData))

    def determineWinner(self):
        totalWins = 0
        for draw in self.drawOrder:
            for board in self.boards:
                wasWinner = board.winner
                won = board.mark(draw)
                if won and not wasWinner:
                    totalWins += 1
                    #we want the last winner
                    if totalWins == len(self.boards):
                        return board.winningScore(draw)

    def __repr__(self):
        lines = []
        lines.append(','.join([str(x) for x in self.drawOrder]))
        lines.extend([repr(board) for board in self.boards])
        return '\n\n'.join(lines)

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleBoard = BoardCollection()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/4/part2/example.txt')
    breakpoint()
    exampleBoard.processInput(lines)
    score = exampleBoard.determineWinner()
    assert score == 1924

    inputBoard = BoardCollection()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/4/part2/input.txt')
    inputBoard.processInput(lines)
    print(f'final score of winning board: {inputBoard.determineWinner()}')


