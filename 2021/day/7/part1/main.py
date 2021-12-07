import collections

class Lanternfish:
    def __init__(self, initialTimer):
        self.internalTimer = initialTimer

    def passDay(self):
        """
        Pass a day of the fish
        :return: True if we spawn a new fish, false otherwise
        """
        spawnNew = False
        if self.internalTimer == 0:
            spawnNew = True
            self.internalTimer = 6
        else:
            self.internalTimer -= 1

        return spawnNew

    def __repr__(self):
        return f'{self.internalTimer}'

class LanternfishSchool:
    def __init__(self):
        self.school = []

    def processInput(self, input):
        initialState = [int(x) for x in input[0].strip().split(',')]
        self.school = [Lanternfish(x) for x in initialState]

    def passDays(self, numDays=80):
        print(f'Initial state: {self}')
        for i in range(numDays):
            self.passDay()
            if i < 18:
                print(f'After {i+1:2} days: {self}')

    def passDay(self):
        for lanternfish in self.school:
            spawnNew = lanternfish.passDay()
            if spawnNew:
                self.school.append(Lanternfish(9))


    def __repr__(self):
        return ','.join([repr(fish) for fish in self.school])

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleSchool = LanternfishSchool()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/6/part1/example.txt')
    breakpoint()
    exampleSchool.processInput(lines)
    exampleSchool.passDays()
    totalLanterns = len(exampleSchool.school)
    assert totalLanterns == 5934

    inputSchool = LanternfishSchool()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/6/part1/input.txt')
    inputSchool.processInput(lines)
    inputSchool.passDays()
    print(f'totalLanterns: {len(inputSchool.school)}')


