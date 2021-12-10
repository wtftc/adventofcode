import collections

class HeightMap:
    def __init__(self, heightMap):
        self.heightMap = heightMap
        self.cols = len(heightMap)
        self.rows = len(heightMap[0])


    @classmethod
    def processInput(cls, input):
        heightMap = []
        for line in input:
            heightMap.append([int(x) for x in line.strip()])
        #transpose so we're row major
        heightMap = list(map(list, zip(*heightMap)))
        return HeightMap(heightMap)

    def adjacentHeights(self, x, y):
        heights = []
        print(f'({x},{y})')
        if x == 0:
            if y == 0:
                heights.extend([self.heightMap[x+1][y], self.heightMap[x][y+1]])
            elif y == self.rows - 1:
                heights.extend([self.heightMap[x+1][y], self.heightMap[x][y-1]])
            else:
                heights.extend([self.heightMap[x+1][y], self.heightMap[x][y-1], self.heightMap[x][y+1]])
        elif x == self.cols - 1:
            if y == 0:
                heights.extend([self.heightMap[x-1][y], self.heightMap[x][y+1]])
            elif y == self.rows - 1:
                heights.extend([self.heightMap[x-1][y], self.heightMap[x][y-1]])
            else:
                heights.extend([self.heightMap[x-1][y], self.heightMap[x][y-1], self.heightMap[x][y+1]])
        else:
            if y == 0:
                heights.extend([self.heightMap[x-1][y], self.heightMap[x+1][y], self.heightMap[x][y+1]])
            elif y == self.rows - 1:
                heights.extend([self.heightMap[x-1][y], self.heightMap[x+1][y], self.heightMap[x][y-1]])
            else:
                heights.extend([self.heightMap[x-1][y], self.heightMap[x+1][y], self.heightMap[x][y-1], self.heightMap[x][y+1]])

        return heights

    def lowPoints(self):
        lowPoints = {}
        for x in range(self.cols):
            for y in range(self.rows):
                curPoint = self.heightMap[x][y]
                if curPoint < min(self.adjacentHeights(x, y)):
                    lowPoints[(x, y)] = curPoint
        return lowPoints

    def riskLevel(self):
        lowPoints = self.lowPoints()
        return sum([x+1 for x in lowPoints.values()])

    def __repr__(self):
        output = []
        heightMap = list(map(list, zip(*self.heightMap)))
        for line in heightMap:
            output.append(''.join(line))
        return '\n'.join(output)

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/9/part1/example.txt')
    breakpoint()
    exampleHeightMap = HeightMap.processInput(lines)
    riskLevel = exampleHeightMap.riskLevel()
    assert riskLevel == 15

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/9/part1/input.txt')
    inputHeightMap = HeightMap.processInput(lines)
    riskLevel = inputHeightMap.riskLevel()
    print(f'riskLevel: {riskLevel}')


