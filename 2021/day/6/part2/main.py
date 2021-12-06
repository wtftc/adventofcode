import collections
import tqdm

class LanternfishSchool:
    def __init__(self):
        self.school = collections.defaultdict(int)

    def processInput(self, input):
        initialState = [int(x) for x in input[0].strip().split(',')]
        for timer in initialState:
            self.school[timer] += 1

    def passDays(self, numDays=80):
        print(f'Initial state: {self}')
        for i in tqdm.tqdm(range(numDays)):
            self.passDay()

    def passDay(self):
        newSchool = collections.defaultdict(int)
        for timer, count in self.school.items():
            if timer == 0:
                newSchool[8] += count
                newSchool[6] += count
            else:
                newSchool[timer - 1] += count

        self.school = newSchool

    def totalFish(self):
        total = 0
        for count in self.school.values():
            total += count
        return total

    def __repr__(self):
        return f'total: {self.totalFish():,}, {self.school}'

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleSchool = LanternfishSchool()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/6/part2/example.txt')
    breakpoint()
    exampleSchool.processInput(lines)
    exampleSchool.passDays(numDays=256)
    totalLanterns = exampleSchool.totalFish()
    assert totalLanterns == 26984457539

    inputSchool = LanternfishSchool()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/6/part2/input.txt')
    inputSchool.processInput(lines)
    inputSchool.passDays(numDays=256)
    print(f'totalLanterns: {inputSchool.totalFish()}')