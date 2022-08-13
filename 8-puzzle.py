""" Name:- Shubham kumar
    Roll No:- 2211CS16
    Dept:- Computer Science and Engineering """
from dfs import DFS
from bfs import BFS


def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle):
    invCount = getInvCount([elem for row in puzzle for elem in row])
    return invCount % 2 == 0


if __name__ == "__main__":
    puzzleSize = 3
    print("Enter Start State: ")
    start = []
    for i in range(puzzleSize):
        start.append(list(map(int, input().strip().split())))
    print("Enter Goal State: ")
    goal = []
    for i in range(puzzleSize):
        goal.append(list(map(int, input().strip().split())))
    if isSolvable(start):

        algo = int(input("Enter 1 for BFS and 2 for DFS: "))
        # start = [[3, 2, 1], [4, 5, 6], [8, 7, 0]]
        # goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if algo == 1:
            x = BFS(start, goal)
            calculateTime = x.bfs(start)
            print(f"BFS algorithms takes {calculateTime} second to execute")
        elif algo == 2:
            calculateTime = DFS(start, goal).dfs(start)
            print(f"DFS algorithms takes {calculateTime} second to execute")
        else:
            print("Invalid Choice")
    else:
        print("Puzzle is not solvable")
