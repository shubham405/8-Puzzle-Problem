class PrintNode:
    def printExploredNode(node):
        for row in node:
            for elem in row:
                print(elem, end=" ")
            print()
        print()
    def printDetails(generation,node):
        n=3
        newNode = [node[i:i + n] for i in range(0, len(node), n)]
        print("generation = ", generation)
        PrintNode.printExploredNode(newNode)


