import collections

class Submarine:
    def __init__(self):
        self.data = []
        self.onesCount = collections.defaultdict(int)
        self.zeroesCount = collections.defaultdict(int)
        self.lineLength = 0

    def gammaRate(self, decimal=True):
        g = ''
        for i in range(self.lineLength):
            if self.onesCount.get(i, 0) > self.zeroesCount.get(i, 0):
                g += '1'
            else:
                g+= '0'
        return int(g, 2) if decimal else g

    def epsilonRate(self, decimal=True):
        e = ''
        for i in range(self.lineLength):
            if self.onesCount.get(i, 0) < self.zeroesCount.get(i, 0):
                e += '1'
            else:
                e += '0'
        return int(e, 2) if decimal else e

    def powerConsumption(self):
        return self.gammaRate() * self.epsilonRate()

    def processInput(self, data):
        self.lineLength = len(data[0].strip())

        for line in data:
            line = line.strip()
            for pos, c in enumerate(line):
                if c == '0':
                    self.zeroesCount[pos] += 1
                else:
                    self.onesCount[pos] += 1

    def __repr__(self):
        return f'gammaRate: {self.gammaRate(decimal=False)}, epsilonRate: {self.epsilonRate(decimal=False)}, powerConsumption: {self.powerConsumption()}'


def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleSub = Submarine()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/3/part1/example.txt')
    breakpoint()
    exampleSub.processInput(lines)
    assert exampleSub.powerConsumption() == 198

    inputSub = Submarine()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/3/part1/input.txt')
    inputSub.processInput(lines)
    print(f'input sub power consumption: {inputSub.powerConsumption()}')


