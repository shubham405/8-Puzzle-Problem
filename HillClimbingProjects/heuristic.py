import random
def heurestcCalculation(node,huresticType,endGoal):
    ans = 0
    #print(huresticType)
    if huresticType == "missTiles":
        for i in range(3):
            for j in range(3):
                if node[i][j] != endGoal[i][j] and node[i][j]!=0:
                    ans += 1
    if huresticType == "manhattan":
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if node[i][j] == endGoal[k][l] and node[i][j]!=0:
                            ans += abs(i - k) + abs(j - l)
        #print(f"manhatten = {ans}")
    if huresticType == "notAdmissible":
        ans = random.randint(0, 100)+25
        #print(ans)
    #print(ans)
    return ans

