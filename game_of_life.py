from Coordinate import Coordinate

class GamePlayer:

    def __init__(self, aliveCells, maxSteps, gridTopLeftCoordinate, gridX, gridY):
        self.aliveCells = []
        self.maxSteps = maxSteps
        self.gridX = gridX
        self.gridY = gridY

        for cell in self.aliveCells:
            coordinate = Coordinate(cell[0],cell[1])
            self.aliveCells.append(coordinate)

    def printCurrentGridState(self):
        cellCount = 0
        for y in range(self.gridY):
            lineOfCells = ""
            for x in range(self.gridX):
                coordinate = (x,y)
            print(lineOfCells)

    def getAdjacentLiveCoordinatesCount(self, coordinate):
        adjacentLiveCoordinates = []
        adjacentCoordinates = coordinate.getAdjacentCoordinates()
        for coordinate in adjacentCoordinates:
            location = (coordinate.x, coordinate.y)
            if location in self.aliveCells:
                adjacentLiveCoordinates.append(location)
        return len(adjacentLiveCoordinates)

    def nextGenerationIsAlive(self, coordinate):
        liveNeighbourCount = self.getAdjacentLiveCoordinatesCount(coordinate)
        if 2 <= liveNeighbourCount <= 3:
            return True
        elif liveNeighbourCount == 3:
            return True
        else: 
            return False

    def simulateStep(self):
        nextGenerationOfAliveCells = []
        for cell in self.aliveCells:
            if self.nextGenerationIsAlive(cell):
                nextGenerationOfAliveCells.append(cell)
        self.aliveCells = nextGenerationOfAliveCells


    def playGame(self):
        for step in range(self.maxSteps):
            self.printCurrentGridState()
            self.simulateStep()
        return self.aliveCells

initialLiveCells = [(1,1),(0,1),(2,1)]
gridTopLeftCoordinate = [0,0]
gridBottomRightCoordinate = [4,4]
game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
aliveCells = game.playGame()
print(aliveCells)