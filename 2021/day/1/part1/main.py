import pandas as pd

def readInput(filename="C:/Users/bill/Code/projects/adventofcode/2021/day/1/part1/input.txt"):
    df = pd.read_csv(filename)
    return df

def countIncreasing(df):
    dfd = df.diff()
    increasing = len(dfd[dfd.v > 0])
    print(f"Increasing values: {increasing}")
    return increasing

if __name__ == "__main__":
    df = readInput(filename="C:/Users/bill/Code/projects/adventofcode/2021/day/1/part2/example.txt")
    increasing = countIncreasing(df)
    assert increasing == 7

    df = readInput()
    countIncreasing(df)


