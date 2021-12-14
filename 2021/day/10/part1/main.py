import collections

class NavSubsystemLine:
    expectedMap = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>',
    }
    scoreMap = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    def __init__(self, line):
        self.line = line
        #error: (expected, found)
        self.errors = []
        self.parse()

    def parse(self):
        stack = []
        for c in self.line:
            if c in {'[', '(', '{', '<'}:
                stack.append(c)
            elif c in {']', ')', '}', '>'}:
                if len(stack) > 0:
                    open = stack.pop()
                    expected = self.expectedMap[open]
                    if c != expected:
                        self.errors.append((expected, c))

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
        return sum([l.score() for l in self.lines])

    def __repr__(self):
        return '\n'.join(str(l) for l in self.lines)

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/10/part1/example.txt')
    breakpoint()
    exampleNavSubsystem = NavSubsystem.processInput(lines)
    score = exampleNavSubsystem.totalScore()
    assert score == 26397

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/10/part1/input.txt')
    inputNavSubsystem = NavSubsystem.processInput(lines)
    score = inputNavSubsystem.totalScore()
    print(f'score: {score}')


