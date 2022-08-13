class PrintNode:
    def printExploredNode(node,steps,algo):
        print(f"  {algo} step {steps}:   ")
        for row in node:
            for elem in row:
                print(elem, end=" ")
            print()
        print()