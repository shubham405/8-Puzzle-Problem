import random
from heuristic import heuresticCalculation
from printNode import PrintNode
class GeneticAlgo:
    def __init__(self, goalNode, popSize,heurestic):
        self.population = []
        self.goalNode = goalNode
        self.populationSize = popSize
        self.mutationRate = 0.1
        self.state = []
        self.heurestic=heurestic
        # creating population
        for i in range(popSize):
            self.state = []
            while len(self.state) < 9:
                x=random.randint(0,8)
                if x not in self.state:
                    self.state.append(x)

            self.population.append(self.state)

    def selection(self):
        self.population.sort(key=lambda x: heuresticCalculation(x, self.heurestic, self.goalNode))
        newPopulation = self.population[:60]
        samples = random.sample(self.population[60:], 2)
        for i in range(len(samples)):
            newPopulation.append(samples[i])
        self.population = newPopulation

    def crossover(self):
        # making child with new population
        for i in range(100 - len(self.population)):
            parent = random.sample(self.population, 2)
            newChild = []
            x = 0
            y = 0
            while len(newChild) < 9:
                probablity = random.random()
                if probablity < 0.6:
                    if x+5<9:
                        for v in range(5 + x):
                            if len(newChild) < 9:
                                if parent[0][v] not in newChild:
                                    newChild.append(parent[0][v])
                    if 5-y>=0:
                        for v in range(5 - y, 9):
                            if len(newChild) < 9:
                                if parent[1][v] not in newChild:
                                    newChild.append(parent[1][v])
                else:
                    if x + 5 < 9:
                        for v in range(5 + x):
                            if len(newChild) < 9:
                                if parent[1][v] not in newChild:
                                    newChild.append(parent[1][v])
                    if 5 - y >= 0:

                        for v in range(5 - y, 9):
                            if len(newChild) < 9:
                                if parent[0][v] not in newChild:
                                    newChild.append(parent[0][v])
                x += 1
                y += 1
            self.population.append(newChild)

    def mutate(self):
        newPopulation = []
        for samples in self.population:
            mutation = []
            for i in samples:
                if random.random() < self.mutationRate:
                    x=random.randint(0, 8)
                    if x not in mutation:
                        mutation.append(x)
                else:
                    if i not in mutation:
                        mutation.append(i)
            while len(mutation) < 9:
                for x in range(9):
                    if x not in mutation:
                        mutation.append(x)
            newPopulation.append(mutation)
        self.population = newPopulation

    def solve(self):
        generation = 0
        while True:
            generation += 1
            x = self.population[0]
            PrintNode.printDetails(generation, x)
            if heuresticCalculation(x, self.heurestic, self.goalNode) == 0:
                return ["solution found", generation, x]
            elif generation > 1000:
                return ["solution not found", generation, x]
            self.selection()
            self.crossover()
            self.mutate()





