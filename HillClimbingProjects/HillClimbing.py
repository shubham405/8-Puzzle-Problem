import heapq
from copy import deepcopy
from heuristic import heurestcCalculation
from main import Node
from printNode import PrintNode
import time


class HeuresticImpl:
    def __init__(self, start, goal, monotonic=None):
        self.start = start
        self.goal = goal
        self.visited = {}
        self.queue = []
        self.monotonic = monotonic

    def goLeft(self, row, col, currNode, heurestic, goal):
        # curHeurestics = currNode.total - currNode.gValue
        dataNode = deepcopy(currNode)
        if col > 0:
            # print(self.visited)
            dataNode[row][col], dataNode[row][col - 1] = dataNode[row][col - 1], dataNode[row][col]
            misTiles = heurestcCalculation(dataNode, heurestic, goal)
            return [misTiles, dataNode]
        else:

            return [99999]

    def goRight(self, row, col, currNode, heurestic, goal):
        #curHeurestics = currNode.total - currNode.gValue
        dataNode = deepcopy(currNode)
        if col < len(dataNode) - 1:
            # print(self.visited)
            dataNode[row][col], dataNode[row][col + 1] = dataNode[row][col + 1], dataNode[row][col]
            misTiles = heurestcCalculation(dataNode, heurestic, goal)
            return [misTiles, dataNode]
        else:
            return [99999]

    def goUp(self, row, col, currNode, heurestic, goal):
        # curHeurestics = currNode.total - currNode.gValue
        dataNode = deepcopy(currNode)
        if row > 0:
            # print(self.visited)
            dataNode[row][col], dataNode[row - 1][col] = dataNode[row - 1][col], dataNode[row][col]
            misTiles = heurestcCalculation(dataNode, heurestic, goal)
            return [ misTiles, dataNode]
        else:
            return [99999]

    def goDown(self, row, col, currNode, heurestic, goal):
        dataNode = deepcopy(currNode)
        # curHeurestics= currNode.total-currNode.gValue
        if row < len(dataNode) - 1:
            # print(self.visited)
            dataNode[row][col], dataNode[row + 1][col] = dataNode[row + 1][col], dataNode[row][col]
            misTiles = heurestcCalculation(dataNode, heurestic, goal)
            return [misTiles, dataNode]
        else:
            return [99999]

    def calculatePath(self, node, heurestic):

        shoulder = 0
        steps = 0
        totalNodeExplored = 0
        startTime = time.time()
        currNode = node
        data = currNode.data
        path = []
        f_n_value = currNode.total
        h_value = (heurestcCalculation(data, heurestic, self.goal))
        while shoulder < 100:

            if data == self.goal:
                endTime = time.time()
                totalTimeTaken = endTime - startTime
                totalTimeTaken = round(totalTimeTaken, 2)
                return [steps, totalNodeExplored, path, totalTimeTaken]

            for row in range(len(data)):
                for col in range(len(data)):
                    if data[row][col] == 0:
                        down = self.goDown(row, col, data, heurestic, self.goal)
                        left = self.goLeft(row, col, data, heurestic, self.goal)
                        right = self.goRight(row, col, data, heurestic, self.goal)
                        up = self.goUp(row, col, data, heurestic, self.goal)
            c_hurestic = min(left[0], right[0], up[0], down[0])
            #print(left[0],right[0],up[0],down[0])
            #print("c_hurestic= ",c_hurestic, "h_value= ",h_value)
            print(c_hurestic)
            if c_hurestic > h_value:
                endTime = time.time()
                totalTimeTaken = endTime - startTime
                totalTimeTaken = round(totalTimeTaken, 2)
                return [-1, totalTimeTaken]
            if c_hurestic == h_value:
                shoulder += 1
            else:
                shoulder = 0
            h_value = c_hurestic
            totalNodeExplored += 1
            if c_hurestic == down[0]:
                path.append('Down')
                data = down[1]
                PrintNode.printExploredNode(data)
                continue
            if c_hurestic == left[0]:
                data = left[1]
                PrintNode.printExploredNode(data)
                path.append('Left')
                continue
            if c_hurestic == right[0]:
                data = right[1]
                PrintNode.printExploredNode(data)
                path.append('Right')
                continue


            if c_hurestic == up[0]:
                data = up[1]
                PrintNode.printExploredNode(data)
                path.append('Up')
                continue


        endTime = time.time()
        totalTimeTaken = endTime - startTime
        totalTimeTaken = round(totalTimeTaken, 2)
        return [-2, totalTimeTaken]
