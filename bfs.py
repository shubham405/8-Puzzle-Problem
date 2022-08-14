from copy import deepcopy
from collections import deque
import time
from printNode import PrintNode


# BFS class
class BFS:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.visited = {}
        self.queue = deque()

    def goLeft(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go left or not
        if col > 0:
            curNode[row][col - 1], curNode[row][col] = curNode[row][col], curNode[row][col - 1]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.queue.append(curNode)

    def goRight(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go right or not
        if col < len(curNode) - 1:
            curNode[row][col + 1], curNode[row][col] = curNode[row][col], curNode[row][col + 1]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.queue.append(curNode)

    def goUp(self, node, row, col):
        curNode = deepcopy(node)
        # check if we can go up or not
        if row > 0:
            curNode[row - 1][col], curNode[row][col] = curNode[row][col], curNode[row - 1][col]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node]=1
            self.queue.append(curNode)

    def goDown(self, node, row, col):
        curNode = deepcopy(node)

        # check if we can go down or not
        if row < len(curNode) - 1:
            curNode[row + 1][col], curNode[row][col] = curNode[row][col], curNode[row + 1][col]
            node = tuple(map(tuple, curNode))
            if node in self.visited.keys():
                return
            self.visited[node] = 1
            self.queue.append(curNode)

    def bfs(self, node):
        self.queue.append(node)
        curNode=node
        node = tuple(map(tuple, node))
        self.visited[node]=1
        countSteps = 0
        startTime = time.time()

        while len(self.queue) != 0:
            countSteps = countSteps + 1
            currentNode = self.queue.popleft()
            #PrintNode.printExploredNode(currentNode,countSteps,"BFS")
            if currentNode == self.goal:
                endTime = time.time()
                totalTimeTaken = endTime - startTime
                totalTimeTaken = round(totalTimeTaken, 2)
                return [countSteps,totalTimeTaken]
            for row in range(len(currentNode)):
                for col in range(len(currentNode)):
                    if currentNode[row][col] == 0:
                        self.goLeft(currentNode, row, col)
                        self.goDown(currentNode, row, col)
                        self.goRight(currentNode, row, col)
                        self.goUp(currentNode, row, col)
