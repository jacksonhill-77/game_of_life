class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getAdjacentCells(self):
        adjacentCells = []
        for y in range(self.y - 1, self.y + 2):
            for x in range (self.x - 1, self.x + 2):
                if (x,y) == (self.x, self.y):
                    continue
                adjacentCells.append(Cell(x, y))
        return adjacentCells

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True

