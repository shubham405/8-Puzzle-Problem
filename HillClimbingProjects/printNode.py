class PrintNode:
    def printExploredNode(node):
        for row in node:
            for elem in row:
                print(elem, end=" ")
            print()
        print()
