import collections

class CrabSwarm:
    def __init__(self):
        self.swarm = []

    def processInput(self, input):
        initialState = [int(x) for x in input[0].strip().split(',')]
        self.swarm = initialState
        self.minPos = min(initialState)
        self.maxPos = max(initialState)

    def alignPositionCost(self, newPos):
        """
        Align crabs to new position
        :param newPos: the new position to align to
        :return: the fuel cost to align to the position
        """
        return sum([abs(self.swarm[i]-newPos) for i in range(len(self.swarm))])

    def findMinAlignmentCost(self):
        minCost = 100000000000000000
        minPos = -1
        for pos in range(self.minPos, self.maxPos):
            fuelCost = self.alignPositionCost(pos)
            if fuelCost < minCost:
                minCost = fuelCost
                minPos = pos

        return minPos, minCost

    def __repr__(self):
        return ','.join([repr(crab) for crab in self.swarm])

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleSwarm = CrabSwarm()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/7/part1/example.txt')
    breakpoint()
    exampleSwarm.processInput(lines)
    minPos, minCost = exampleSwarm.findMinAlignmentCost()
    assert minCost == 37
    assert minPos == 2

    inputSwarm = CrabSwarm()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/7/part1/input.txt')
    inputSwarm.processInput(lines)
    minPos, minCost = inputSwarm.findMinAlignmentCost()
    print(f'minPos: {minPos} minCost: {minCost}')


