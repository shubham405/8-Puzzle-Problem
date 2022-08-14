class PrintNode:
    def printExploredNode(node, steps, algo, failed=False):
        if not failed:
            print(f"  {algo} step {steps}:   ")
        for row in node:
            for elem in row:
                print(elem, end=" ")
            print()
        print()
