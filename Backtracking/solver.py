# basic grid to solve (correct tests will be made later)
gridToSolve = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
               [5, 2, 0, 0, 0, 0, 0, 0, 0],
               [0, 8, 7, 0, 0, 0, 0, 3, 1],
               [0, 0, 3, 0, 1, 0, 0, 8, 0],
               [9, 0, 0, 8, 6, 3, 0, 0, 5],
               [0, 5, 0, 0, 9, 0, 6, 0, 0],
               [1, 3, 0, 0, 0, 0, 2, 5, 0],
               [0, 0, 0, 0, 0, 0, 0, 7, 4],
               [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def printSolvedGrid(grid):
    print("\nGrid solved : \n")
    for row in grid:
        print(row)
    print("\n")


# Asserts if the grid is fully solved or not (for recursivity) and solves the grid
def solveGrid(grid):
    # When there is no more free case, the grid is solved
    row, col, boolean = findFreeCase(grid)
    if not boolean:
        return True

    for num in range(1, 10):
        if canPutNumberHere(grid, row, col, num):
            grid[row][col] = num

            if solveGrid(grid):
                return True
            else:
                grid[row][col] = 0

    return False


# Allows us to find the coordinates of the first empty case (and assign them to variables in solveGrid)
def findFreeCase(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col, True
    return 0, 0, False


# Asserts if the given number is used in the given row
def usedInGivenRow(grid, row, num):
    for col in range(9):
        if grid[row][col] == num:
            return True
    return False


# Asserts if the given number is used in the given col
def usedInGivenCol(grid, col, num):
    for row in range(9):
        if grid[row][col] == num:
            return True
    return False


# Asserts if the given number is used in the given box (3 * 3 cases)
def usedInBox(grid, startingRow, startingCol, num):
    for row in range(3):
        for col in range(3):
            if grid[row + startingRow][col + startingCol] == num:
                return True
    return False


# Asserts if we can put the given number in the given case
def canPutNumberHere(grid, row, col, num):
    return not usedInBox(grid, row - row % 3, col - col % 3, num) \
           and not usedInGivenCol(grid, col, num) \
           and not usedInGivenRow(grid, row, num) \
           and grid[row][col] == 0


# Used for tests
def getSolvedGrid(grid):
    solveGrid(grid)
    return grid


if solveGrid(gridToSolve):
    print("\nI found a solution !")
    printSolvedGrid(gridToSolve)
else:
    print("No solution found !")
