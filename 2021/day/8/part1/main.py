import collections

class ReadoutEntry:
    def __init__(self, signalPatterns, outputValues):
        self.signalPatterns = signalPatterns
        self.outputValues = outputValues


    @classmethod
    def processInput(cls, input):
        signalPatterns, outputValues = input.strip().split('|')
        signalPatterns = signalPatterns.strip().split(' ')
        outputValues = outputValues.strip().split(' ')
        return ReadoutEntry(signalPatterns, outputValues)

    def __repr__(self):
        return f'{" ".join(self.signalPatterns)} | {" ".join(self.outputValues)}'

class SubmarineReadout:
    def __init__(self, readouts):
        self.readouts = readouts

    @classmethod
    def processInput(cls, input):
        readouts = [ReadoutEntry.processInput(line) for line in input]
        return SubmarineReadout(readouts)

    def countUniqueOutputs(self):
        uniqueOutputs = 0
        for entry in self.readouts:
            uniqueOutputs += len([x for x in entry.outputValues if len(x) in {2, 4, 3, 7}])

        return uniqueOutputs

    def __repr__(self):
        return '\n'.join([repr(entry) for entry in self.readouts])

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/8/part1/example.txt')
    breakpoint()
    exampleReadout = SubmarineReadout.processInput(lines)
    uniqueOutputs = exampleReadout.countUniqueOutputs()
    assert uniqueOutputs == 26

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/8/part1/input.txt')
    inputReadout = SubmarineReadout.processInput(lines)
    uniqueOutputs = inputReadout.countUniqueOutputs()
    print(f'uniqueOutputs: {uniqueOutputs}')


