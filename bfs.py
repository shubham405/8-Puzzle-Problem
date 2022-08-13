from copy import deepcopy
from collections import deque
import time
from printNode import PrintNode


# BFS class
class BFS:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.visited = []
        self.queue = deque()

    def goLeft(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go left or not
        if col > 0:
            curNode[row][col - 1], curNode[row][col] = curNode[row][col], curNode[row][col - 1]
            if curNode in self.visited:
                return
            self.visited.append(curNode)
            self.queue.append(curNode)

    def goRight(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go right or not
        if col < len(curNode) - 1:
            curNode[row][col + 1], curNode[row][col] = curNode[row][col], curNode[row][col + 1]
            if curNode in self.visited:
                return
            self.visited.append(curNode)
            self.queue.append(curNode)

    def goUp(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go up or not
        if row > 0:
            curNode[row - 1][col], curNode[row][col] = curNode[row][col], curNode[row - 1][col]
            if curNode in self.visited:
                return
            self.visited.append(curNode)
            self.queue.append(curNode)

    def goDown(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go down or not
        if row < len(curNode) - 1:
            curNode[row + 1][col], curNode[row][col] = curNode[row][col], curNode[row + 1][col]
            if curNode in self.visited:
                return
            self.visited.append(curNode)
            self.queue.append(curNode)

    def bfs(self, node):
        self.queue.append(node)
        countSteps = 0
        startTime = int(time.time())

        while len(self.queue) != 0:
            countSteps = countSteps + 1
            currentNode = self.queue.popleft()
            PrintNode.printExploredNode(currentNode,countSteps)
            if currentNode == self.goal:
                print(f"BFS Solved Puzzle in {countSteps} steps")
                endTime = int(time.time())
                totalTimeTaken = endTime - startTime
                return totalTimeTaken
            for row in range(len(currentNode)):
                for col in range(len(currentNode)):
                    if currentNode[row][col] == 0:
                        self.goLeft(currentNode, row, col)
                        self.goDown(currentNode, row, col)
                        self.goRight(currentNode, row, col)
                        self.goUp(currentNode, row, col)
