import collections
import math

class NavSubsystemLine:
    expectedMap = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>',
    }

    scoreMap = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    def __init__(self, line):
        self.line = line
        #error: (expected, found)
        self.errors = []
        self.stack = []
        self.parse()

    def parse(self):
        for c in self.line:
            if c in {'[', '(', '{', '<'}:
                self.stack.append(c)
            elif c in {']', ')', '}', '>'}:
                if len(self.stack) > 0:
                    open = self.stack.pop()
                    expected = self.expectedMap[open]
                    if c != expected:
                        self.errors.append((expected, c))

    def incompleteClosingScore(self):
        if len(self.errors) != 0:
            return 0

        closing = []
        while len(self.stack) > 0:
            open = self.stack.pop()
            closing.append(self.expectedMap[open])

        score = 0
        for c in closing:
            score *= 5
            score += self.scoreMap[c]

        return score

    def score(self):
        if len(self.errors) == 0:
            return 0
        else:
            firstExpected, firstFound = self.errors[0]
            return self.scoreMap[firstFound]

    def createErrorMessage(self, expected, found):
        return f"Expected {expected}, but found {found} instead."

    def __repr__(self):
        return self.line


class NavSubsystem:
    def __init__(self, lines):
        self.lines = lines

    @classmethod
    def processInput(cls, input):
        lines = [NavSubsystemLine(x.strip()) for x in input]
        return NavSubsystem(lines)

    def totalScore(self):
        incompleteScore = [l.incompleteClosingScore() for l in self.lines]
        incompleteScore = list(sorted(filter(lambda x: x != 0, incompleteScore)))
        return incompleteScore[math.floor(len(incompleteScore)/2)]

    def __repr__(self):
        return '\n'.join(str(l) for l in self.lines)

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/10/part2/example.txt')
    breakpoint()
    exampleNavSubsystem = NavSubsystem.processInput(lines)
    score = exampleNavSubsystem.totalScore()
    assert score == 288957

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/10/part2/input.txt')
    inputNavSubsystem = NavSubsystem.processInput(lines)
    score = inputNavSubsystem.totalScore()
    print(f'score: {score}')


