class Submarine:
    def __init__(self, startHorizontal=0, startDepth=0, startAim=0):
        self.horizontal = startHorizontal
        self.depth = startDepth
        self.aim = startAim

    def forward(self, v):
        self.horizontal += v
        self.depth += (self.aim * v)

    def down(self, v):
        self.aim += v

    def up(self, v):
        self.aim -= v

    def position(self):
        return self.horizontal * self.depth

    def __repr__(self):
        return f'horizontal: {self.horizontal}, depth: {self.depth}, aim: {self.aim}, position: {self.position()}'

def readFile(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def moveSub(sub, directions):
    for line in directions:
        direction, v = line.split(' ')
        v = int(v)
        if direction == 'forward':
            sub.forward(v)
        elif direction == 'down':
            sub.down(v)
        elif direction == 'up':
            sub.up(v)
        else:
            raise ValueError('unknown direction v')

if __name__ == '__main__':
    exampleSub = Submarine()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/2/part1/example.txt')
    breakpoint()
    moveSub(exampleSub, lines)
    assert exampleSub.position() == 900

    inputSub = Submarine()
    lines = readFile('C:/Users/bill/Code/projects/adventofcode/2021/day/2/part1/input.txt')
    moveSub(inputSub, lines)
    print(f'input sub position: {inputSub.position()}')


