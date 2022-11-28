from Coordinate import Coordinate

class GamePlayer:

    def __init__(self, aliveCells, maxSteps, gridTopLeftCoordinate, gridX, gridY):
        self.aliveCells = []
        self.maxSteps = maxSteps
        self.gridX = gridX
        self.gridY = gridY

        for cell in aliveCells:
            coordinate = Coordinate(cell[0],cell[1])
            self.aliveCells.append(coordinate)

    def printCurrentGridState(self):
        cellCount = 0
        for y in range(self.gridY):
            lineOfCells = ""
            for x in range(self.gridX):
                coordinate = (x,y)
            print(lineOfCells)

    def printCoordinatesAsTuples(self, listOfCoordinates):
        if len(listOfCoordinates) == 0:
            print("No cells")
        for cell in listOfCoordinates:
            print(cell.x,cell.y)

    def getAdjacentLiveCoordinates(self, coordinate):
        adjacentLiveCoordinates = []
        adjacentCoordinates = coordinate.getAdjacentCoordinates()
        for coordinate in adjacentCoordinates:
            for cell in self.aliveCells:
                if coordinate == cell:
                    adjacentLiveCoordinates.append(coordinate)
        return adjacentLiveCoordinates

    def doesCellSurvive(self, cell):
        liveNeighbours = self.getAdjacentLiveCoordinates(cell)
        liveNeighbourCount = len(liveNeighbours)
        if 2 <= liveNeighbourCount <= 3:
            print("Alive")
            return True
        else: 
            print("Dead")
            return False

    def determineIfEachCellSurvives(self, cellsWeNeedToLookAt):
        print("Input cells")
        print(len(cellsWeNeedToLookAt))
        cellsThatSurvive = []
        print("Cells we're looking at")
        for cell in cellsWeNeedToLookAt:
            print(cell.x,cell.y)
        for cell in cellsWeNeedToLookAt:
            if self.doesCellSurvive(cell) == True:
                cellsThatSurvive.append(cell)
        print("Cells that survive:")
        print(len(cellsThatSurvive))
        return cellsThatSurvive

    def findAllCellsToLookAt(self):
        cellsWeNeedToLookAt = []
        for cell in self.aliveCells:
            if cell not in cellsWeNeedToLookAt:
                cellsWeNeedToLookAt.append(cell)
            for adjacentCoordinate in cell.getAdjacentCoordinates():
                if adjacentCoordinate not in cellsWeNeedToLookAt:
                    cellsWeNeedToLookAt.append(adjacentCoordinate)
        return cellsWeNeedToLookAt

    def simulateStep(self):
        self.printCoordinatesAsTuples(self.aliveCells)
        cellsWeNeedToLookAt = self.findAllCellsToLookAt()
        print("Length of cells")
        print(len(cellsWeNeedToLookAt))
        nextGenerationAliveCells = self.determineIfEachCellSurvives(cellsWeNeedToLookAt)
        self.aliveCells = nextGenerationAliveCells
        print("Length of alive cells")
        print(len(self.aliveCells))

    def playGame(self):
        for step in range(self.maxSteps):
            print("\nStep " + str(step))
            self.simulateStep()
        return self.aliveCells

initialLiveCells = [(1,1),(0,1),(2,1)]
game = GamePlayer(initialLiveCells, 2, [0,0], 5,5)
output = game.playGame()