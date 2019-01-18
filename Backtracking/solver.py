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
varRow, varCol = 0, 0


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


print_toSolve()
print(varCol)
print(varRow)
print(findFreeCase(gridToSolve))
print(varCol)
print(varRow)
