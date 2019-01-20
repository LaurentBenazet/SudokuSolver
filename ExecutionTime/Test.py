import time


def timeTestV1():
    from Backtracking.solver import getSolvedGrid
    start = time.time()
    getSolvedGrid([[0, 3, 0, 0, 0, 1, 2, 0, 5],
                   [8, 1, 0, 3, 0, 0, 0, 6, 0],
                   [9, 4, 0, 0, 0, 0, 0, 0, 3],
                   [0, 0, 0, 2, 1, 0, 0, 0, 9],
                   [0, 0, 0, 0, 0, 0, 0, 3, 0],
                   [0, 0, 0, 0, 0, 9, 7, 5, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 7, 4, 6, 0, 0, 0],
                   [3, 0, 0, 0, 0, 2, 0, 4, 6]])
    end = time.time()
    return end - start


def timeTestV2():
    from BacktrackingV2.solver import solver
    start = time.time()
    grid = [[0, 3, 0, 0, 0, 1, 2, 0, 5],
            [8, 1, 0, 3, 0, 0, 0, 6, 0],
            [9, 4, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 2, 1, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 9, 7, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 4, 6, 0, 0, 0],
            [3, 0, 0, 0, 0, 2, 0, 4, 6]]
    solver(grid)
    end = time.time()
    return end - start


# Returns the mean time taken for nbTests execution of each solver
def meanTime(nbTests):
    countV1 = 0
    countV2 = 0
    for i in range(nbTests):
        countV1 += timeTestV1()
        countV2 += timeTestV2()
    countV1 = countV1 / nbTests
    countV2 = countV2 / nbTests
    print("Mean for " + str(nbTests) + " tries on backtracking V1 : " + str(countV1) + "s\nMean for " + str(
        nbTests) + " tries on backtracking V2 : " + str(countV2) + "s")


meanTime(100)
