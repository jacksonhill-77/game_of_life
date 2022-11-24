class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getAdjacentCoordinates(coordinates):
    adjacentCoordinates = set()
    for coordinate in coordinates:
        for x in range(coordinate.x - 1, 2):
            for y in range (coordinate.y - 1, 2):
                adjacentCoordinates.add(Coordinate(x, y))
    return adjacentCoordinates

class GamePlayer:

    def __init__(self, aliveCells, maxSteps):
        self.aliveCells = aliveCells
        self.maxSteps = maxSteps

    def countAdjacentLiveCells(self, cell):
        pass
        # Incomplete

    def nextGenerationIsAlive(self, coordinate):
        liveNeighbourCount = self.countAdjacentLivecoordinates(coordinate)
        if self.isAlive(coordinate) == True and 2 <= liveNeighbourCount <= 3:
            return True
        elif self.isAlive(coordinate) == False and liveNeighbourCount == 3:
            return True
        else: 
            return False


    def simulateStep(self):
        nextGenerationOfAliveCells = []
        coordinatesWeNeedToLookAt = self.getAdjacentCoordinates(self.aliveCells)
        for coordinate in coordinatesWeNeedToLookAt:
            if (self.nextGenerationIsAlive(coordinate)):
                nextGenerationOfAliveCells.append(coordinate)
        self.aliveCells = nextGenerationOfAliveCells
            

    def playGame(self):
        for _step in range(self.maxSteps):
            self.simulateStep()
        return self.aliveCells

userInput = [(1,1),(0,1),(2,1)]
game = GamePlayer(userInput, 5)
game.playGame()