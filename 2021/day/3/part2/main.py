import collections

class Submarine:
    def __init__(self):
        self.data = []
        self.onesList = collections.defaultdict(list)
        self.zeroesList = collections.defaultdict(list)
        self.lineLength = 0

    def oxygenRating(self, decimal=True):
        oxygenList = None
        for i in range(self.lineLength):
            if oxygenList is None:
                onesList = self.onesList.get(i, [])
                zeroesList = self.zeroesList.get(i, [])
            else:
                zeroesList = []
                onesList = []
                for line in oxygenList:
                    if line[i] == '0':
                        zeroesList.append(line)
                    else:
                        onesList.append(line)

            if len(onesList) >= len(zeroesList):
                oxygenList = onesList
            else:
                oxygenList = zeroesList

                if len(oxygenList) == 1:
                    break

        oxygenRating = oxygenList[0]
        return int(oxygenRating, 2) if decimal else oxygenRating

    def co2ScrubberRating(self, decimal=True):
        co2ScrubberList = None
        for i in range(self.lineLength):
            if co2ScrubberList is None:
                onesList = self.onesList.get(i, [])
                zeroesList = self.zeroesList.get(i, [])
            else:
                zeroesList = []
                onesList = []
                for line in co2ScrubberList:
                    if line[i] == '0':
                        zeroesList.append(line)
                    else:
                        onesList.append(line)

            if len(onesList) < len(zeroesList):
                co2ScrubberList = onesList
            else:
                co2ScrubberList = zeroesList

            if len(co2ScrubberList) == 1:
                break

        co2ScrubberRating = co2ScrubberList[0]
        return int(co2ScrubberRating, 2) if decimal else co2ScrubberRating

    def lifeSupportRating(self):
        return self.oxygenRating() * self.co2ScrubberRating()

    def processInput(self, data):
        self.lineLength = len(data[0].strip())
        self.data = data

        for line in data:
            line = line.strip()
            for pos, c in enumerate(line):
                if c == '0':
                    self.zeroesList[pos].append(line)
                else:
                    self.onesList[pos].append(line)

    def __repr__(self):
        return f'oxygenRating: {self.oxygenRating(decimal=False)}, co2ScrubberRating: {self.co2ScrubberRating(decimal=False)}, lifeSupportRating: {self.lifeSupportRating()}'

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleSub = Submarine()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/3/part2/example.txt')
    breakpoint()
    exampleSub.processInput(lines)
    assert exampleSub.lifeSupportRating() == 230

    inputSub = Submarine()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/3/part2/input.txt')
    inputSub.processInput(lines)
    print(f'input sub power consumption: {inputSub.lifeSupportRating()}')


