def printSolvedGrid(grid):
    print("\nGrid solved : \n")
    for row in grid:
        print(row)
    print("\n")


# This code isn't very clean, every function isn't meant to be inner and private, but it does what I created it for
# This function is the core of the solver, with every function used
def solver(grid):
    # this grid contains every number possible for each case of the grid at the beginning of the solving
    possibilitiesGrid = [[[] for _ in range(9)] for _ in range(9)]

    # Asserts if the grid is fully solved or not (for recursivity) and solves the grid
    def _inner_solveGrid(grid):
        # When there is no more free case, the grid is solved
        row, col, boolean = _inner_findFreeCase(grid)
        if not boolean:
            return True

        # we take only number possible for this case (it is more optimized)
        for num in possibilitiesGrid[row][col]:
            # this verification is useful during recursion (because possibilitiesGrid isn't updated)
            if _inner_canPutNumberHere(grid, row, col, num):
                grid[row][col] = num

                if _inner_solveGrid(grid):
                    return True
                else:
                    grid[row][col] = 0
        return False

    # Allows us to find the coordinates of the first empty case (and assign them to variables in solveGrid)
    def _inner_findFreeCase(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    return row, col, True
        return 0, 0, False

    # Asserts if the given number is used in the given row
    def _inner_usedInGivenRow(grid, row, num):
        for col in range(9):
            if grid[row][col] == num:
                return True
        return False

    # Asserts if the given number is used in the given col
    def _inner_usedInGivenCol(grid, col, num):
        for row in range(9):
            if grid[row][col] == num:
                return True
        return False

    # Asserts if the given number is used in the given box (3 * 3 cases)
    def _inner_usedInBox(grid, startingRow, startingCol, num):
        for row in range(3):
            for col in range(3):
                if grid[row + startingRow][col + startingCol] == num:
                    return True
        return False

    # Asserts if we can put the given number in the given case
    def _inner_canPutNumberHere(grid, row, col, num):
        return not _inner_usedInBox(grid, row - row % 3, col - col % 3, num) \
               and not _inner_usedInGivenCol(grid, col, num) \
               and not _inner_usedInGivenRow(grid, row, num) \
               and grid[row][col] == 0

    # main part of the solver

    # initialization of possibilitesGrid
    for num in range(1, 10):
        for row in range(9):
            for col in range(9):
                if _inner_canPutNumberHere(grid, row, col, num):
                    possibilitiesGrid[row][col].append(num)

    _inner_solveGrid(grid)
    return grid
