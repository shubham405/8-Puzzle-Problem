""" 8 Puzzle Problem """
import random

from printNode import PrintNode
from dfs import DFS
from bfs import BFS


def getInvCount(arr):
    inv_count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != 0 and arr[i] != 0 and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle):
    invCount = getInvCount([elem for row in puzzle for elem in row])
    return invCount % 2 == 0


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
    if isSolvable(start):

        # algo = int(input("Enter 1 for BFS and 2 for DFS: "))
        # # start = [[3, 2, 1], [4, 5, 6], [8, 7, 0]]
        # # goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        # if algo == 1:
        print("Initial State of Puzzle")
        PrintNode.printExploredNode(start, 0, 0, True)
        print("Please Wait.....")
        callBfs = BFS(start, goal)
        calculateBFS = callBfs.bfs(start)
        callDfs = DFS(start, goal)
        calculateDFS = callDfs.dfs(start)
        print(f"BFS algorithms takes {calculateBFS[0]} steps & {calculateBFS[1]} second to execute")
        print(f"DFS algorithms takes {calculateDFS[0]} steps & {calculateDFS[1]} second to execute")
        stepDiff = calculateBFS[0] - calculateDFS[0]
        if calculateDFS[0] < calculateBFS[0]:

            print(f"BFS take {abs(stepDiff)} steps more than DFS ")
        elif calculateBFS[0] < calculateDFS[0]:
            print(f"DFS take {abs(stepDiff)} steps more than BFS ")
        else:
            print("Both take equal number of steps")


    else:
        PrintNode.printExploredNode(start, 0, 0, True)
        print("This Puzzle is not solvable")
