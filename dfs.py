from copy import deepcopy
from collections import deque
import time
from printNode import PrintNode


# DFS class
class DFS:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.visited = {}
        self.stack = deque()

    def goLeft(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go left or not
        if col > 0:
            curNode[row][col - 1], curNode[row][col] = curNode[row][col], curNode[row][col - 1]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.stack.append(curNode)

    def goRight(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go right or not
        if col < len(curNode) - 1:
            curNode[row][col + 1], curNode[row][col] = curNode[row][col], curNode[row][col + 1]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.stack.append(curNode)

    def goUp(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go up or not
        if row > 0:
            curNode[row - 1][col], curNode[row][col] = curNode[row][col], curNode[row - 1][col]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.stack.append(curNode)

    def goDown(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go down or not
        if row < len(curNode) - 1:
            curNode[row + 1][col], curNode[row][col] = curNode[row][col], curNode[row + 1][col]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.stack.append(curNode)

    def dfs(self, node):
        self.stack.append(node)
        countSteps = 0
        timeNow = time.time()
        while len(self.stack) != 0:
            countSteps = countSteps + 1
            curNode = self.stack.pop()
            PrintNode.printExploredNode(curNode, countSteps,"DFS")
            if curNode == self.goal:
                totalTimeTaken = time.time() - timeNow
                totalTimeTaken=round(totalTimeTaken,2)
                return [countSteps,totalTimeTaken]
            for row in range(len(curNode)):
                for col in range(len(curNode)):
                    if curNode[row][col] == 0:
                        self.goLeft(curNode, row, col)
                        self.goRight(curNode, row, col)
                        self.goUp(curNode, row, col)
                        self.goDown(curNode, row, col)
