from Cell import Cell

class GamePlayer:

    def __init__(self, aliveCells, maxSteps, gridOrigin, gridX, gridY):
        self.aliveCells = []
        self.maxSteps = maxSteps
        self.gridX = gridX
        self.gridY = gridY
        self.gridOriginX = gridOrigin[0]
        self.gridOriginY = gridOrigin[1]

        for cell in aliveCells:
            newCell = Cell(cell[0],cell[1])
            self.aliveCells.append(newCell)

    def printCurrentGridState(self):
        for y in range(self.gridOriginY, self.gridY):
            lineOfCells = ""
            for x in range(self.gridOriginX, self.gridX):
                cell = Cell(x,y)
                if cell in self.aliveCells:
                    lineOfCells += "O "
                else:
                    lineOfCells += "- "
            print(lineOfCells)

    def printCellsAsTuples(self, listOfCells):
        if len(listOfCells) == 0:
            print("No cells")
        else: 
            for cell in listOfCells:
                print(cell.x,cell.y)

    def getAdjacentLiveCells(self, cell):
        adjacentLiveCells = []
        adjacentCells = cell.getAdjacentCells()
        for adjacentCell in adjacentCells:
            for aliveCell in self.aliveCells:
                if adjacentCell == aliveCell:
                    adjacentLiveCells.append(cell)
        return adjacentLiveCells

    def doesCellSurvive(self, cell):
        liveNeighbourCount = len(self.getAdjacentLiveCells(cell))
        if cell not in self.aliveCells and liveNeighbourCount == 3:
            return True
        elif cell in self.aliveCells and 2 <= liveNeighbourCount <= 3:
            return True
        else: 
            return False

    def determineIfEachCellSurvives(self, cellsWeNeedToLookAt):
        cellsThatSurvive = []
        for cell in cellsWeNeedToLookAt:
            if self.doesCellSurvive(cell) == True:
                cellsThatSurvive.append(cell)
        return cellsThatSurvive

    def findAllCellsToLookAt(self):
        cellsWeNeedToLookAt = []
        for cell in self.aliveCells:
            if cell not in cellsWeNeedToLookAt:
                cellsWeNeedToLookAt.append(cell)
            for adjacentCell in cell.getAdjacentCells():
                if adjacentCell not in cellsWeNeedToLookAt:
                    cellsWeNeedToLookAt.append(adjacentCell)
        return cellsWeNeedToLookAt

    def simulateStep(self):
        cellsWeNeedToLookAt = self.findAllCellsToLookAt()
        nextGenerationOfAliveCells = self.determineIfEachCellSurvives(cellsWeNeedToLookAt)
        self.aliveCells = nextGenerationOfAliveCells

    def playGame(self):
        for step in range(self.maxSteps):
            self.printCurrentGridState()
            print("\nStep " + str(step))
            self.simulateStep()
        return self.aliveCells

initialLiveCells = [(1,1),(0,1),(2,1)]
game = GamePlayer(initialLiveCells, 2, [0,0], 5,5)
output = game.playGame()