from printNode import PrintNode
from geneticAlgoImpl import GeneticAlgo
import time


class Node:
    def __init__(self):
        self.state = {}
        self.h = 0
        self.g = 0
        self.parent = None

    def __eq__(self, other):
        return self.__class__ == other.__class__


if __name__ == '__main__':
    puzzleSize = int(input("Enter N value in N*N size puzzle: "))
    start = []
    goal = []
    print("Enter Start State: ")
    for i in range(3):
        start.append(list(map(int, input().strip().split())))
        if len(start[i]) > 3:
            print("Wrong input provided")
            exit(0)
    print("Enter Goal State: ")

    for i in range(3):
        goal.append(list(map(int, input().strip().split())))
        if len(goal[i]) > 3:
            print("Wrong input provided")
            exit(0)
    print("Initial State of Puzzle")
    PrintNode.printExploredNode(start)

    print("Goal state")
    PrintNode.printExploredNode(goal)
    startList = []
    goalList = []
    for i in range(3):
        for j in range(3):
            startList.append(start[i][j])
    for i in range(3):
        for j in range(3):
            goalList.append(goal[i][j])
    mistiles =  GeneticAlgo(goalList,100,"missTiles")
    startTime = time.time()
    resMisstiles=mistiles.solve()
    endTime = time.time()
    totalTimeTaken = endTime - startTime
    totalTimeTaken = round(totalTimeTaken, 2)


    manhatten =  GeneticAlgo(goalList,1000,"manhattan")
    startTime = time.time()
    resManhatten = manhatten.solve()
    endTime = time.time()
    totalTimeTaken = endTime - startTime
    totalTimeTaken = round(totalTimeTaken, 2)
    print("Results for miss placed tiles ")
    print(f" {resMisstiles[0]}\ntotal generation = {resMisstiles[1]} \n ")
    print("Total time taken = ", totalTimeTaken)
    print()
    print("Results for Manhattan distances")
    print(f" {resManhatten[0]}\ntotal generation = {resManhatten[1]} \n ")
    print("Total time taken = ", totalTimeTaken)
