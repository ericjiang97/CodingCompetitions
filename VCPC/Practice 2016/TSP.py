# Town A - Town B, E, D - Index 0
# Town B - Town A, C, D  - Index 1
# Town C - Towns B, D - Index 2
# Town D - Town A, B,E - Index 3
# Town E = Town A, D - Index 4

adjcencyTable = [[1,3,4],[0,2,3],[1,3],[0,1,4],[1,3]]

def backtracking(partial,n,listofsolutions,nexttoTowns):
    if(len(partial)==n):
        listofsolutions.append(partial.copy())
    else:
        possible = getPossibleTowns(partial,n,listofsolutions,nexttoTowns)
        for connectedTowns in possible:
            partial.append(connectedTowns)
            backtracking(partial,n,listofsolutions,nexttoTowns)
            print(partial)
            partial.pop()

def getPossibleTowns(partial,n,listofsolutions,nexttoTowns):
    listofsolutions = []
    if(len(partial)>0):
        lastTown = partial[len(partial)-1]
        for value in nexttoTowns[lastTown]:
            if(value not in listofsolutions):
                listofsolutions.append(value)
    else:
        listofsolutions.append(0)
    return listofsolutions

solutionslist = []
backtracking([],len(adjcencyTable),solutionslist,adjcencyTable)
print(solutionslist)