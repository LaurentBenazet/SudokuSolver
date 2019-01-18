# basic grid to solve (correct tests will be made later)
gridToSolve = [[9, 0, 0, 1, 0, 0, 0, 0, 5],
               [0, 0, 5, 0, 9, 0, 2, 0, 1],
               [8, 0, 0, 0, 4, 0, 0, 0, 0],
               [0, 0, 0, 0, 8, 0, 0, 0, 0],
               [0, 0, 0, 7, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 2, 6, 0, 0, 9],
               [2, 0, 0, 3, 0, 0, 0, 0, 6],
               [0, 0, 0, 2, 0, 0, 9, 0, 0],
               [0, 0, 1, 9, 0, 4, 5, 7, 0]]

# They will be used to find the first empty case
varRow, varCol = -1, -1


def print_toSolve():
    print("Grid to solve \n")
    for a in gridToSolve:
        print(a)
    print("\n")


# Allows us to find the coordinates of the first empty case (and assign them to variables defined above)
def findFreeCase(grid):
    global varRow
    global varCol
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                varRow = row
                varCol = col
                return True
    return False


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
    return not usedInBox(grid, row, col, num) \
           and not usedInGivenCol(grid, col, num) \
           and not usedInGivenRow(grid, row, num) \
           and grid[row][col] == 0


print_toSolve()
print(varCol)
print(varRow)
print(findFreeCase(gridToSolve))
print(varCol)
print(varRow)
