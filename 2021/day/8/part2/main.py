import collections

class ReadoutEntry:
    def __init__(self, signalPatterns, outputValues):
        self.signalPatterns = signalPatterns
        self.signalPatternSets = [set(x) for x in signalPatterns]
        self.outputValues = outputValues
        self.outputValueSets = [set(x) for x in outputValues]

    def determineDigits(self):
        self.one = one = next(filter(lambda x: len(x) == 2, self.signalPatternSets))
        self.seven = seven = next(filter(lambda x: len(x) == 3, self.signalPatternSets))
        self.four = four = next(filter(lambda x: len(x) == 4, self.signalPatternSets))
        self.eight = eight = next(filter(lambda x: len(x) == 7, self.signalPatternSets))

        top = seven.difference(one).pop()
        lenSixes = list(filter(lambda x: len(x) == 6, self.signalPatternSets))
        lenFives = list(filter(lambda x: len(x) == 5, self.signalPatternSets))
        topRightOrMiddleOrBottomLeft = lenSixes[0].difference(lenSixes[1]).union(lenSixes[1].difference(lenSixes[0])).union(lenSixes[1].difference(lenSixes[2]))
        bottomRight = one.difference(topRightOrMiddleOrBottomLeft).pop()
        topRight = one.difference(bottomRight).pop()
        middleOrBottomLeft = topRightOrMiddleOrBottomLeft.difference(topRight)
        middle = four.intersection(middleOrBottomLeft).pop()
        bottomLeft = middleOrBottomLeft.difference(middle).pop()
        topLeft = four.difference(one).difference(middle).pop()
        bottom = eight.difference(top+topLeft+topRight+middle+bottomLeft+bottomRight).pop()

        self.two = set(top+topRight+middle+bottomLeft+bottom)
        self.three = set(top+topRight+middle+bottomRight+bottom)
        self.five = set(top+topLeft+middle+bottomRight+bottom)
        self.six = set(top+topLeft+middle+bottomLeft+bottomRight+bottom)
        self.nine = set(top+topLeft+topRight+middle+bottomRight+bottom)
        self.zero = set(top+topLeft+topRight+bottomLeft+bottomRight+bottom)

    def computeOutput(self):
        self.determineDigits()
        outputStr = ''
        for outputVal in self.outputValueSets:
            if outputVal == self.zero:
                outputStr += '0'
            if outputVal == self.one:
                outputStr += '1'
            if outputVal == self.two:
                outputStr += '2'
            if outputVal == self.three:
                outputStr += '3'
            if outputVal == self.four:
                outputStr += '4'
            if outputVal == self.five:
                outputStr += '5'
            if outputVal == self.six:
                outputStr += '6'
            if outputVal == self.seven:
                outputStr += '7'
            if outputVal == self.eight:
                outputStr += '8'
            if outputVal == self.nine:
                outputStr += '9'
        return int(outputStr)

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

    def outputTotal(self):
        total = 0
        for entry in self.readouts:
            total += entry.computeOutput()
        return total

    def __repr__(self):
        return '\n'.join([repr(entry) for entry in self.readouts])

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/8/part2/example.txt')
    breakpoint()
    testReadout = SubmarineReadout.processInput(['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'])
    testReadout.outputTotal()

    exampleReadout = SubmarineReadout.processInput(lines)
    totalOutputs = exampleReadout.outputTotal()
    assert totalOutputs == 61229

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/8/part2/input.txt')
    inputReadout = SubmarineReadout.processInput(lines)
    totalOutputs = inputReadout.outputTotal()
    print(f'totalOutputs: {totalOutputs}')


