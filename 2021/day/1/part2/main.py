import pandas as pd

def readInput(filename="C:/Users/bill/Code/projects/adventofcode/2021/day/1/part2/input.txt"):
    df = pd.read_csv(filename)
    return df

def rollingSum(df, window=3):
    """
    https://stackoverflow.com/questions/28288252/fast-rolling-sum-for-list-of-data-vectors-2d-matrix
    """
    ret = df.cumsum()
    sub = ret[window:].reset_index(drop=True) - ret[:-window].reset_index(drop=True)
    sub = sub.set_index(pd.RangeIndex(start=window, stop=len(ret)))
    ret[window:] = sub
    return ret[window-1:]

def countIncreasing(df):
    dfd = df.diff()
    increasing = len(dfd[dfd.v > 0])

    return increasing

if __name__ == "__main__":
    df = readInput(filename="C:/Users/bill/Code/projects/adventofcode/2021/day/1/part2/example.txt")
    df = rollingSum(df)
    increasing = countIncreasing(df)
    print(f"Example increasing values: {increasing}")
    assert increasing == 5

    df = readInput()
    df = rollingSum(df)
    increasing = countIncreasing(df)
    print(f"Input increasing values: {increasing}")

