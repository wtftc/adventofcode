import collections

LEN_X = 10
LEN_Y = 10
FLASH_ENERGY = 10

class BioluminescentOctopus:
    def __init__(self, initialEnergy, x, y):
        self.energy = initialEnergy
        self.x = x
        self.y = y
        self.flashed = False

    def incrementEnergy(self):
        self.energy += 1
        return self.energy

    def findAdjacent(self):
        adjacent = []
        for deltaX in [-1, 0, 1]:
            for deltaY in [-1, 0, 1]:
                if deltaX == 0 and deltaY == 0:
                    continue
                x = self.x + deltaX
                y = self.y + deltaY

                if x >= 0 and x < LEN_X and y >= 0 and y < LEN_Y:
                    adjacent.append((x, y))

        return adjacent

    def flash(self):
        self.flashed = True

    def finishIteration(self):
        if self.energy >= FLASH_ENERGY and not self.flashed:
            raise ValueError(f"Energy: {self.energy}, but didn't flash")

        self.flashed = False
        self.energy = self.energy if self.energy < FLASH_ENERGY else 0

    def __repr__(self):
        return f'({self.x}, {self.y}), energy: {self.energy}, flashed: {self.flashed}'


class OctoMap:
    def __init__(self, octos):
        self.octos = octos
        self.totalFlashes = 0

    @classmethod
    def processInput(cls, input):
        octos = []
        for x, line in enumerate(input):
            row = []
            for y, energy in enumerate(line.strip()):
                row.append(BioluminescentOctopus(int(energy), x, y))

            octos.append(row)

        return OctoMap(octos)

    def step(self):

        flashed = set()
        for x in range(LEN_X):
            for y in range(LEN_Y):
                octo = self.octos[x][y]
                newEnergy = octo.incrementEnergy()
                if newEnergy >= FLASH_ENERGY:
                    flashed.add(octo)

        while len(flashed) > 0:
            flashedOcto = flashed.pop()
            if flashedOcto.flashed:
                continue
            flashedOcto.flash()
            self.totalFlashes += 1

            adjacent = flashedOcto.findAdjacent()
            for adjX, adjY in adjacent:
                adjOcto = self.octos[adjX][adjY]
                adjEnergy = adjOcto.incrementEnergy()
                if adjEnergy >= FLASH_ENERGY and not adjOcto.flashed:
                    flashed.add(adjOcto)

        for x in range(LEN_X):
            for y in range(LEN_Y):
                self.octos[x][y].finishIteration()

    def iterate(self, count):
        for i in range(count):
            # breakpoint()
            self.step()

    def __repr__(self):
        output = []
        for line in self.octos:
            output.append(','.join([f'{octo.energy:2}' for octo in line]))

        return '\n'.join(output)

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/11/part1/example.txt')
    breakpoint()
    exampleMap = OctoMap.processInput(lines)
    exampleMap.iterate(100)
    flashes = exampleMap.totalFlashes
    assert flashes == 1656

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/11/part1/input.txt')
    inputMap = OctoMap.processInput(lines)
    inputMap.iterate(100)
    flashes = inputMap.totalFlashes
    print(f'flashes: {flashes}')


