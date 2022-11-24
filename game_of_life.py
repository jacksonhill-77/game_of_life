class Cell:

    def __init__(self, x, y):
        self.alive = False
        self.x = x
        self.y = y

class Grid:

    def __init__(self, gridSize, initialAliveCells):
        self.gridSize = gridSize
        self.grid = []
        self.initialAliveCells = initialAliveCells

        for y in range(gridSize):
            cellList = []
            for x in range(gridSize):
                cell = Cell(x, y)
                if (x,y) in initialAliveCells:
                    cell.alive = True
                cellList.append(cell)
            self.grid.append(cellList)

class GamePlayer:

    def __init__(self, gridSize, initialAliveCells, maxSteps):
        self.gridSize = gridSize
        self.grid = Grid(gridSize, initialAliveCells)
        self.maxSteps = maxSteps
        self.aliveCells = []
        self.currentStepGrid = []

    def printCurrentGridState(self):
        cellCount = 0
        for row in self.grid.grid:
            lineOfCells = ""
            for cell in row:
                cellCount += 1
                if cell.alive == True:
                    lineOfCells += "O "
                else:
                    lineOfCells += "- "
            print(lineOfCells)

    def returnAdjacentCellsAsList(self, cell, grid):
        max = self.gridSize - 1
        x = cell.x
        y = cell.y
        adjacentCells = []
        if x > 0 and y > 0:
            upperLeftCell = grid[y-1][x-1]
            adjacentCells.append(upperLeftCell) 
        if y > 0:
            upperCentreCell = grid[y-1][x]
            adjacentCells.append(upperCentreCell)
        if x < max and y > 0:
            upperRightCell = grid[y-1][x+1]
            adjacentCells.append(upperRightCell)
        if x > 0:
            centreLeftCell = grid[y][x-1]
            adjacentCells.append(centreLeftCell) 
        if x < max:
            centreRightCell = grid[y][x+1]
            adjacentCells.append(centreRightCell) 
        if x > 0 and y < max:
            lowerLeftCell = grid[y+1][x-1]
            adjacentCells.append(lowerLeftCell) 
        if y < max:
            lowerCentreCell = grid[y+1][x]
            adjacentCells.append(lowerCentreCell) 
        if x < max and y < max:
            lowerRightCell = grid[y+1][x+1]
            adjacentCells.append(lowerRightCell) 
        return adjacentCells


    def killOrResurrectCell(self, cell, aliveCellsCount):
        newCell = Cell(cell.x,cell.y)
        if cell.alive == True and 2 <= aliveCellsCount <= 3:
            newCell.alive = True
        elif cell.alive == False and aliveCellsCount == 3:
            newCell.alive = True
        else: 
            newCell.alive = False
        return newCell
        

    def getNextCell(self, cell, grid):
        aliveCells = []
        for adjacentCell in self.returnAdjacentCellsAsList(cell, grid):
            if adjacentCell.alive == True:
                aliveCells.append(adjacentCell)
        newCell = self.killOrResurrectCell(cell, len(aliveCells))
        return newCell
        

    def determineNewStatusOfCells(self):
        cellsToInsert = []
        for row in self.grid.grid:
            for cell in row:
                newCell = self.getNextCell(cell, self.grid.grid)
                cellsToInsert.append(newCell)
        return cellsToInsert

    def simulateStep(self):
        cellsToInsert = self.determineNewStatusOfCells()
        for cell in cellsToInsert:
            self.grid.grid[cell.y][cell.x] = cell

    def playGame(self):
        print("Initial grid: ")
        self.printCurrentGridState()
        step = 0
        while step < self.maxSteps:
            step = step + 1
            self.simulateStep()
            self.printCurrentGridState()
        print("Final grid state:")
        self.printCurrentGridState()
        return self.aliveCells

userInput = [(1,1),(0,1),(2,1)]
game = GamePlayer(4,userInput, 5)
game.playGame()