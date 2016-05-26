start = [[6, 5, 3], [2, 4, 8], [7, 0, 1], []]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
STEPS = ['U', 'R', 'D', 'L']
STEPS_HASH = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
POSITIONS = {1:[0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0],
             5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 0: [2, 2]}
achievedGoalNode = []


def compareMatrix(mat):
    if mat[0:3] == goal:
        return True
    else:
        return False


def posNode(x):
    for p in x:
        if 0 in p:
            j = p.index(0)
            i = x.index(p)
            return [i, j]


def sumIndex(x, y):
    p = [-1, -1]
    p[0] = x[0] + y[0]
    p[1] = x[1] + y[1]
    return p


def generator(x, step):
    addIndex = STEPS_HASH.get(step)
    posOld = posNode(x)
    posNew = sumIndex(posOld, addIndex)
    if (posNew[0] > 2) or (posNew[0] < 0) or (posNew[1] > 2) or (posNew[1] < 0):
        return False
    else:
        y = [list(p) for p in x]
        temp = y[posNew[0]][posNew[1]]
        y[posNew[0]][posNew[1]] = y[posOld[0]][posOld[1]]
        y[posOld[0]][posOld[1]] = temp
        y[3].append(step)
        return y
    

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            temp = POSITIONS[state[i][j]]
            distance += abs(temp[0] - i) + abs(temp[1] - j)
    return distance


def aStar(start):
    global achievedGoalNode
    HASH = {}
    HASH[manhattan(start)] = [start]
    found = False
    while (not found):
        minValue = min(HASH)
        currentState = HASH[minValue][0]
        if compareMatrix(currentState) == True:
            achievedGoalNode = currentState
            found = True
        else:
            for step in STEPS:
                newMatrix = generator(currentState, step)
                if newMatrix != False:
                    gValue = len(newMatrix[3])
                    hValue = manhattan(newMatrix)
                    mValue = gValue + hValue
                    if mValue in HASH:
                        HASH[mValue].append(newMatrix)
                    else:
                        HASH[mValue] = [newMatrix]
            if len(HASH[minValue]) == 1:
                HASH.pop(minValue)
            else:
                HASH[minValue].pop(0)

     
aStar(start)
#print (len(achievedGoalNode[3]))
