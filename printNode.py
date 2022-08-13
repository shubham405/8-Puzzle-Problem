class PrintNode:
    def printExploredNode(node,steps):
        print(f"   step {steps}:   ")
        for row in node:
            for elem in row:
                print(elem, end=" ")
            print()
        print()