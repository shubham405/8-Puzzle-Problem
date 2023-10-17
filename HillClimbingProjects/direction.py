


if (row < len(current.data) - 1):
    current.data[row][col], current.data[row + 1][col] = current.data[row + 1][col], \
                                                         current.data[row][col]
    if current.data not in self.visited:
        temp1 = misplacedTiles(current.data)
        if (current.gvalue + temp1 < ans):
            self.queue.append(node(current.data, current.gvalue + 1))
            print("working2")
            heapq.heafify(self.queue)
            self.visited.append(current.data)
    current.data[row][col], current.data[row + 1][col] = current.data[row + 1][col], \
                                                         current.data[row][col]
if (col > 0):
    current.data[row][col], current.data[row][col - 1] = current.data[row][col - 1], \
                                                         current.data[row][col]
    if current.data not in self.visited:
        temp1 = misplacedTiles(current.data)
        if (current.gvalue + temp1 < ans):
            self.queue.append(node(current.data, current.gvalue + 1))
            print("working3")
            heapq.heapify(self.queue)
            self.visited.append(current.data)
    current.data[row][col], current.data[row][col - 1] = current.data[row][col - 1], \
                                                         current.data[row][col]
if (col < len(current.data) - 1):
    current.data[row][col], current.data[row][col + 1] = current.data[row][col + 1], \
                                                         current.data[row][col]
    if current.data not in self.visited:
        temp1 = misplacedTiles(current.data)
        if (current.gvalue + temp1 < ans):
            self.queue.append(node(current.data, current.gvalue + 1))
            print("working4")
            heapq.heapify(self.queue)
            self.visited.append(current.data)
    current.data[row][col], current.data[row][col + 1] = current.data[row][col + 1], \
                                                         current.data[row][col]
