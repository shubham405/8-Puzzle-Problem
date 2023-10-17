import heapq
from copy import deepcopy
from heuristic import heurestcCalculation
from main import Node
import time
from printNode import PrintNode


class HeuresticImpl:
    def __init__(self, start, goal,monotonic=None):
        self.start = start
        self.goal = goal
        self.visited = {}
        self.queue = []
        self.monotonic=monotonic

    def goLeft(self, row, col, currNode, heurestic, goal):
        curHeurestics = currNode.total - currNode.gValue
        dataNode = deepcopy(currNode.data)
        if col > 0:
            # print(self.visited)
            dataNode[row][col], dataNode[row][col - 1] = dataNode[row][col - 1], dataNode[row][col]
            # print(dataNode)
            dictNode = tuple(map(tuple, dataNode))
            if dictNode not in self.visited.keys():
                # print("working df")
                misTiles = heurestcCalculation(dataNode, heurestic, goal)
                if self.monotonic == "m":
                    print(f"parent node heurestic = {curHeurestics} and child node c(n')+h(n') = {1+misTiles}")
                # print(misTiles)
                #totalCost = currNode[2] + 1 + misTiles
                gValue = currNode.gValue + 1
                nodeChild = Node(dataNode, gValue, heurestic, goal, currNode.path + "[D]")
                heapq.heappush(self.queue, nodeChild)
                # print("working1")
                # heapq.heapify(self.queue)

    def goRight(self, row, col, currNode, heurestic, goal):
        curHeurestics = currNode.total - currNode.gValue
        dataNode = deepcopy(currNode.data)
        if col < len(dataNode) - 1:
            # print(self.visited)
            dataNode[row][col], dataNode[row][col + 1] = dataNode[row][col + 1], dataNode[row][col]
            # print(dataNode)
            dictNode = tuple(map(tuple, dataNode))
            if dictNode not in self.visited.keys():
                # print("working df")
                misTiles = heurestcCalculation(dataNode, heurestic, goal)
                if self.monotonic == "m":
                    print(f"parent node heurestic = {curHeurestics} and child node c(n')+h(n') = {1+misTiles}")
                # print(misTiles)
                #totalCost = currNode[2] + 1 + misTiles
                gValue = currNode.gValue + 1
                nodeChild = Node(dataNode, gValue, heurestic, goal, currNode.path + "[R]")
                heapq.heappush(self.queue, nodeChild)
                # self.queue.append((totalCost, dataNode, gValue))
                # print("working1")
                # heapq.heapify(self.queue)

    def goUp(self, row, col, currNode, heurestic, goal):
        curHeurestics = currNode.total - currNode.gValue
        dataNode = deepcopy(currNode.data)
        if row > 0:
            # print(self.visited)
            dataNode[row][col], dataNode[row - 1][col] = dataNode[row - 1][col], dataNode[row][col]
            # print(dataNode)
            dictNode = tuple(map(tuple, dataNode))
            if dictNode not in self.visited.keys():
                # print("working df")
                misTiles = heurestcCalculation(dataNode, heurestic, goal)
                if self.monotonic == "m":
                    print(f"parent node heurestic = {curHeurestics} and child node c(n')+h(n') = {1+misTiles}")
                # print(misTiles)
                #totalCost = currNode.gValue + 1 + misTiles
                gValue = currNode.gValue + 1
                nodeChild = Node(dataNode, gValue, heurestic, goal, currNode.path + "[U]")
                heapq.heappush(self.queue, nodeChild)
                # self.queue.append((totalCost, dataNode, gValue))
                # print("working1")
                # heapq.heapify(self.queue)

    def goDown(self, row, col, currNode, heurestic, goal):
        dataNode = deepcopy(currNode.data)
        curHeurestics= currNode.total-currNode.gValue
        if row < len(dataNode) - 1:
            # print(self.visited)
            dataNode[row][col], dataNode[row + 1][col] = dataNode[row + 1][col], dataNode[row][col]
            # print(dataNode)
            dictNode = tuple(map(tuple, dataNode))
            if dictNode not in self.visited.keys():
                # print("working df")
                misTiles = heurestcCalculation(dataNode, heurestic, goal)
                if self.monotonic == "m":
                    print(f"parent node heurestic = {curHeurestics} and child node c(n')+h(n') = {1+misTiles}")
                # print(misTiles)
                #totalCost = currNode[2] + 1 + misTiles
                gValue = currNode.gValue + 1
                nodeChild = Node(dataNode, gValue, heurestic, goal, currNode.path + "[D]")
                heapq.heappush(self.queue, nodeChild)
                # self.queue.append((totalCost, dataNode, gValue))
                # print("working1")

    def calculatePath(self, node, heurestic):
        # starth=hueristic(self.start)
        self.queue.append(node)
        heapq.heapify(self.queue)
        ans = -1
        totalNodeExplored = 0
        startTime = time.time()
        while len(self.queue) > 0:
            #print(totalNodeExplored)
            currNode = heapq.heappop(self.queue)
            f_n_value = currNode.total
            data = currNode.data
            dictNode = tuple(map(tuple, data))
            if dictNode not in self.visited.keys():
                # PrintNode.printExploredNode(data)
                totalNodeExplored += 1
                self.visited[dictNode] = 1
                if data == self.goal:
                    endTime = time.time()
                    totalTimeTaken = endTime - startTime
                    totalTimeTaken = round(totalTimeTaken, 2)
                    return [f_n_value, totalNodeExplored,currNode,totalTimeTaken]
                for row in range(len(data)):
                    for col in range(len(data)):
                        if data[row][col] == 0:
                            self.goDown(row, col, currNode, heurestic, self.goal)
                            self.goLeft(row, col, currNode, heurestic, self.goal)
                            self.goRight(row, col, currNode, heurestic, self.goal)
                            self.goUp(row, col, currNode, heurestic, self.goal)
        endTime = time.time()
        totalTimeTaken = endTime - startTime
        totalTimeTaken = round(totalTimeTaken, 2)
        return [ans, totalNodeExplored,totalTimeTaken]
