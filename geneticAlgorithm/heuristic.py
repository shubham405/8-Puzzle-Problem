import random


def heuresticCalculation(node, huresticType, endGoal):
    ans = 0
    node = list(node)
    endGoal = list(endGoal)
    if huresticType == "missTiles":
        for i in range(9):
                if node[i] != endGoal[i] and node[i] != 0:
                    ans += 1
    if huresticType == "manhattan":
        n = 3
        newNode = [node[i:i + n] for i in range(0, len(node), n)]
        goalNode = [endGoal[i:i + n] for i in range(0, len(endGoal), n)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if newNode[i][j] == goalNode[k][l] and newNode[i][j] != 0:
                            ans += abs(i - k) + abs(j - l)
    return ans
