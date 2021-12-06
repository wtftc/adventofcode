import collections

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'{self.x},{self.y}'

class VentLine:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def isDiagonal(self):
        return not (self.startX == self.endX or self.startY == self.endY)

    def allPoints(self):
        if self.startX == self.endX:
            incrementX = 0
        elif self.startX < self.endX:
            incrementX = 1
            r = self.startX - self.endX
        else:
            incrementX = -1
            r = self.startX - self.endX

        if self.startY == self.endY:
            incrementY = 0
        elif self.startY < self.endY:
            incrementY = 1
            r = self.startY - self.endY
        else:
            incrementY = -1
            r = self.startY - self.endY

        return [Point(self.startX + i*incrementX, self.startY + i*incrementY) for i in range(abs(r)+1)]

    @classmethod
    def parse(cls, line):
        start, end = line.strip().split('->')
        startX, startY = start.strip().split(',')
        endX, endY = end.strip().split(',')
        return VentLine(int(startX), int(startY), int(endX), int(endY))

    def __repr__(self):
        return f'{self.startX},{self.startY} -> {self.endX},{self.endY}'

class Map:
    def __init__(self):
        self.lines = []
        self.points = collections.defaultdict(list)
        self.maxX = 0
        self.maxY = 0

    def processInput(self, input):
        for line in input:
            ventLine = VentLine.parse(line)
            self.lines.append(ventLine)
            allPoints = ventLine.allPoints()
            # print(f'{ventLine}: {allPoints}')
            for point in allPoints:
                self.points[point].append(ventLine)
                if point.x > self.maxX:
                    self.maxX = point.x
                if point.y > self.maxY:
                    self.maxY = point.y

    def countOverlaps(self, threshold=2):
        total = 0
        for point, lines in self.points.items():
            if len(lines) >= threshold:
                total += 1

        return total

    def __repr__(self):
        lines = []
        for y in range(self.maxY+1):
            line = ''
            for x in range(self.maxX+1):
                p = Point(x, y)
                ventLines = self.points.get(p)

                if not ventLines:
                    line += '.'
                else:
                    line += f'{len(ventLines)}'
            lines.append(line)
        return '\n'.join(lines)

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    exampleMap = Map()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/5/part2/example.txt')
    breakpoint()
    exampleMap.processInput(lines)
    overlaps = exampleMap.countOverlaps()
    assert overlaps == 12

    inputMap = Map()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/5/part2/input.txt')
    inputMap.processInput(lines)
    print(f'overlaps: {inputMap.countOverlaps()}')


