tabToSolve = [[4, 1, 0, 3, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 2, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 5, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 6, 0, 0]]

solvingTab = [[0 for i in range(9)] for j in range(9)]


def print_solving():
    print("Tableau en train d'être résolu \n")
    for a in solvingTab:
        print(a)
    print("\n")
    print(solvingTab)
    print("\n")


def print_toSolve():
    print("Tableau à résoudre \n")
    for a in tabToSolve:
        print(a)
    print("\n")
    print(tabToSolve)
    print("\n")


print_toSolve()
print_solving()
