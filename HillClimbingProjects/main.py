""" 8 Puzzle Problem using hill climbing"""
import random
from heuristic import heurestcCalculation
from printNode import PrintNode
from HillClimbing import *


class Node:
    def __init__(self, data, gvalue, heurestic, goal, path=""):
        self.data = data
        self.gValue = gvalue
        self.total = heurestcCalculation(data, heurestic, goal)
        self.path = path

    def __repr__(self):
        return f'Node value: {self.total}'

    def __lt__(self, other):
        return self.total < other.total




if __name__ == "__main__":

    puzzleSize = int(input("Enter N value in N*N size puzzle: "))
    choice = input("Enter R for random input and U for user input: ")
    start = []
    goal = []
    if choice == "R":
        randomNumber = list(random.sample(range(0, puzzleSize * puzzleSize), puzzleSize * puzzleSize))
        k = 0
        for i in range(puzzleSize):
            temp = []
            for j in range(puzzleSize):
                temp.append(randomNumber[k])
                k += 1
            start.append(temp)
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    elif choice == "U":
        print("Enter Start State: ")

        for i in range(puzzleSize):
            start.append(list(map(int, input().strip().split())))
            if len(start[i]) > puzzleSize:
                print("Wrong input provided")
                exit(0)
        print("Enter Goal State: ")

        for i in range(puzzleSize):
            goal.append(list(map(int, input().strip().split())))
            if len(goal[i]) > puzzleSize:
                print("Wrong input provided")
                exit(0)

    print("Initial State of Puzzle")
    PrintNode.printExploredNode(start)

    print("Goal state")
    PrintNode.printExploredNode(goal)

    ''' Manhattan distance'''
    print("calculating manhattan distance.....\n")
    callMissPlace = HeuresticImpl(start, goal)
    manhattan = Node(start, 0, "manhattan", goal)
    calculateManhatten = callMissPlace.calculatePath(manhattan, "manhattan")
    if calculateManhatten[0] != -1 and calculateManhatten[0] != -2:
        print("Puzzle solved")
        print(f"total states explored = {calculateManhatten[1]}")
        print(f"Total number of steps to optimal path = {calculateManhatten[1]}")
        print(f'optimal path = "{calculateManhatten[2]}"')
        print(f"optimal path cost = {calculateManhatten[1]}")
        print(f"Time taken for execution = {calculateManhatten[3]}")
        print()
    elif calculateManhatten[0] == -1:
        print("Puzzle stucked at local minima")
        print(f"Time taken for execution = {calculateManhatten[1]}")
        print()
    else:
        print("Puzzle is stucked at plateau")
        print(f"Time taken for execution = {calculateManhatten[1]}")
        print()

    """ misplaced tiles"""
    print("calculating misplaced tiles.....\n")
    callMissPlace = HeuresticImpl(start, goal)
    missTiles = Node(start, 0, "missTiles", goal)
    calculatedMissPlacedTiles = callMissPlace.calculatePath(missTiles, "missTiles")
    if calculatedMissPlacedTiles[0] != -1 and calculatedMissPlacedTiles[0] != -2:
        print("Puzzle solved")
        print(f"total states explored = {calculatedMissPlacedTiles[1]}")
        # print(f"steps taken by  manhatten = {calculatedMissPlacedTiles[0]}")
        print(f"Total number of steps to optimal path = {calculatedMissPlacedTiles[1]}")
        print(f'optimal path = "{calculatedMissPlacedTiles[2]}"')
        print(f"optimal path cost = {calculatedMissPlacedTiles[1]}")
        print(f"Time taken for execution = {calculatedMissPlacedTiles[3]}")
        print()
    elif calculatedMissPlacedTiles[0] == -1:
        print("Puzzle stucked at local mainima")
        print(f"Time taken for execution = {calculatedMissPlacedTiles[1]}")
        print()
    else:
        print("Puzzle is stucked at plateau")
        print(f"Time taken for execution = {calculatedMissPlacedTiles[1]}")
        print()

