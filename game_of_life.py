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

    def printCellProperties(self, cell):
        if cell.alive == False:
            status = "Dead"
        else: status = 'Alive'
        print("x: " + str(cell.x) + " y: " + str(cell.y) + " " + status + "\n")

    def returnAdjacentCellsAsList(self, cell, grid):
        max = self.gridSize - 1
        x = cell.x
        y = cell.y
        adjacentCells = []
        print("\nCurrent cell: " + str(x) + " " + str(y) + " " + str(cell.alive))
        if x > 0 and y > 0:
            upperLeftCell = grid[y-1][x-1]
            print("NW")
            adjacentCells.append(upperLeftCell) 
        if y > 0:
            upperCentreCell = grid[y-1][x]
            print("N")
            adjacentCells.append(upperCentreCell)
        if x < max and y > 0:
            upperRightCell = grid[y-1][x+1]
            print("NE")
            adjacentCells.append(upperRightCell)
        if x > 0:
            centreLeftCell = grid[y][x-1]
            print("W")
            adjacentCells.append(centreLeftCell) 
        if x < max:
            centreRightCell = grid[y][x+1]
            print("E")
            adjacentCells.append(centreRightCell) 
        if x > 0 and y < max:
            lowerLeftCell = grid[y+1][x-1]
            print("SW")
            adjacentCells.append(lowerLeftCell) 
        if y < max:
            lowerCentreCell = grid[y+1][x]
            print("S")
            adjacentCells.append(lowerCentreCell) 
        if x < max and y < max:
            lowerRightCell = grid[y+1][x+1]
            print("SE")
            adjacentCells.append(lowerRightCell) 
        print("Adjacent cells:")
        for cell in adjacentCells:
            print(cell.x,cell.y,cell.alive)
        return adjacentCells


    def killOrResurrectCell(self, cell, aliveCellsCount):
        print("Alive cells: " + str(aliveCellsCount))
        newCell = Cell(cell.x,cell.y)
        if cell.alive == True and 2 <= aliveCellsCount <= 3:
            newCell.alive = True
        elif cell.alive == False and aliveCellsCount == 3:
            newCell.alive = True
        else: 
            newCell.alive = False
        print("Result: " + str(newCell.alive))
        return newCell
        

    def updateCellStatus(self, cell, grid):
        aliveCells = []
        for adjacentCell in self.returnAdjacentCellsAsList(cell, grid):
            if adjacentCell.alive == True:
                aliveCells.append(adjacentCell)
        # print("Current cell:")
        # self.printCellProperties(cell)
        # print("Current grid:")
        # self.printCurrentGridState()
        newCell = self.killOrResurrectCell(cell, len(aliveCells))
        return newCell
        

    def determineNewStatusOfCells(self):
        cellsToInsert = []
        print("FINAL CELL PROPERTIES")
        for row in self.grid.grid:
            for cell in row:
                self.printCellProperties
                self.updateCellStatus(cell, self.grid.grid)
                cellsToInsert.append(cell)
        return cellsToInsert

    def simulateStep(self):
        cellsToInsert = self.determineNewStatusOfCells()
        print("Cells to insert:")

    def playGame(self):
        print("Initial grid: ")
        self.printCurrentGridState()
        step = 0
        while step < self.maxSteps:
            step = step + 1
            print("STEP " + str(step))
            self.simulateStep()
            self.printCurrentGridState()
        print("Final grid state:")
        self.printCurrentGridState()
        return self.aliveCells

userInput = [(0,0),(0,1),(1,1),(0,2)]
# userInput = [(0,1),(1,0),(0,0),(2,2),(0,2),(1,1),(2,1)]
game = GamePlayer(4,userInput, 1)
game.playGame()