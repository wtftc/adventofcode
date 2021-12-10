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

    def adjacentPoints(self, x, y):
        points = []
        if x == 0:
            if y == 0:
                points.extend([(x+1, y), (x, y+1)])
            elif y == self.rows - 1:
                points.extend([(x+1, y), (x,y-1)])
            else:
                points.extend([(x+1, y), (x,y-1), (x,y+1)])
        elif x == self.cols - 1:
            if y == 0:
                points.extend([(x-1,y), (x,y+1)])
            elif y == self.rows - 1:
                points.extend([(x-1,y), (x,y-1)])
            else:
                points.extend([(x-1,y), (x,y-1), (x,y+1)])
        else:
            if y == 0:
                points.extend([(x-1,y), (x+1,y), (x,y+1)])
            elif y == self.rows - 1:
                points.extend([(x-1,y), (x+1,y), (x,y-1)])
            else:
                points.extend([(x-1,y), (x+1,y), (x,y-1), (x,y+1)])

        return points

    def findBasis(self):
        basinStarts = {}
        basins = collections.defaultdict(set)
        for y in range(self.rows):
            for x in range(self.cols):
                curPoint = self.heightMap[x][y]
                coordinates = (x, y)
                if curPoint < 9:
                    adjacentPoints = self.adjacentPoints(x, y)
                    newBasin = True
                    for p in adjacentPoints:
                        pointStart = basinStarts.get(p)
                        if pointStart:
                            if coordinates not in basinStarts:
                                basinStarts[coordinates] = pointStart
                                basins[pointStart].add(coordinates)
                                newBasin = False
                            elif basinStarts[coordinates] != pointStart:
                                #merge basins
                                firstStart = basinStarts[coordinates]
                                secondStart = pointStart
                                if firstStart[0] < secondStart[0]:
                                    usedStart = firstStart
                                    removedStart = secondStart
                                elif secondStart[0] < firstStart[0]:
                                    usedStart = secondStart
                                    removedStart = firstStart
                                else: #same x coordinate
                                    if firstStart[1] < secondStart[1]:
                                        usedStart = firstStart
                                        removedStart = secondStart
                                    else:
                                        usedStart = secondStart
                                        removedStart = firstStart

                                #move all basin points from removed start to the used start basin
                                removedPoints = basins[removedStart]
                                startPoints = basins[usedStart]
                                del basins[removedStart]
                                for p in removedPoints:
                                    basinStarts[p] = usedStart
                                    if p not in startPoints:
                                        startPoints.add(p)

                                #mark coordinates of newest basin point
                                basinStarts[coordinates] = usedStart
                                if coordinates not in startPoints:
                                    startPoints.add(coordinates)

                    if newBasin:
                        basinStarts[coordinates] = coordinates
                        basins[coordinates].add(coordinates)

        breakpoint()
        return basins

    def largestSizes(self, count=3):
        basins = self.findBasis()
        basinStarts = list(basins.keys())
        basinStarts = sorted(basinStarts, key=lambda x: len(basins[x]))

        size = 1
        for x in basinStarts[-count:]:
            size *= len(basins[x])
        return size

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
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/9/part2/example.txt')
    breakpoint()
    exampleHeightMap = HeightMap.processInput(lines)
    largestSizes = exampleHeightMap.largestSizes()
    assert largestSizes == 1134

    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/9/part2/input.txt')
    inputHeightMap = HeightMap.processInput(lines)
    largestSizes = inputHeightMap.largestSizes()
    print(f'largestSizes: {largestSizes}')


