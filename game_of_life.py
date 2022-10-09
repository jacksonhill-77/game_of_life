'''Conway's game of life on an infinite grid, optimised for sparse finite life

In Conway's game of life, there's a square grid, where every cell has eight 
neighbours (sides, up and down, and diagonals). 

Every cell is either alive or dead. We're going to assume almost all cells 
are dead, and at the beginning of the game the user will provide a list of 
all the cell coordinates that are alive.

On each step of the game,
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell. (reproduction)
3. All other live cells die in the next generation (under- or over-population),
and all other dead cells stay dead.

As well as the list of live cells, the user will specify the number of steps 
the game should run for. At the end, the game will print the list of live cells.

Extension (if you want it) is to let the user specify a rectangular section of 
the grid and (using ascii art or otherwise) show the state of the game within 
that rectangle on each step of the game (kind of like an animation). (Note: 
any life that ends up outside the rectangle should still be listed at the end 
of the game.)

You can get some inspiration for possible test cases here: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns
'''

from tkinter import N


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

    def printCurrentGridState(self):
        for line in self.grid.grid:
            lineOfCells = ""
            for cell in line:
                if cell.alive == True:
                    lineOfCells += "O "
                else:
                    lineOfCells += "- "
            print(lineOfCells)

    def returnAdjacentCellsAsList(self, cell):
        grid = self.grid.grid
        max = self.gridSize - 1
        x = cell.x
        y = cell.y
        adjacentCells = []
        adjacentCellsLocation = ""
        if x > 0 and y > 0:
            upperLeftCell = grid[y-1][x-1]
            adjacentCells.append(upperLeftCell) 
        if y > 0:
            upperCentreCell = grid[y-1][x]
            adjacentCells.append(upperCentreCell)
        if x < max and y > 0:
            upperRightCell = grid[x+1][y-1]
            adjacentCells.append(upperRightCell)
        if x > 0:
            centreLeftCell = grid[x-1][y]
            adjacentCells.append(centreLeftCell) 
        if x < max:
            centreRightCell = grid[x+1][y]
            adjacentCells.append(centreRightCell) 
        if x > 0 and y < max:
            lowerLeftCell = grid[x-1][y+1]
            adjacentCells.append(lowerLeftCell) 
        if y < max:
            lowerCentreCell = grid[x][y+1]
            adjacentCells.append(lowerCentreCell) 
        if x < max and y < max:
            lowerRightCell = grid[x+1][y+1]
            adjacentCells.append(lowerRightCell) 
        # print(str(x) + " " + str(y) + '. Adjacent cells: ' + str(len(adjacentCells)) + ", " + adjacentCellsLocation)
        # print("Adjacent cells:")
        # for cell in adjacentCells:
        #     print(cell.x,cell.y,cell.alive)
        return adjacentCells


    def killOrResurrectCell(self, cell, aliveCells):
        print("\nCurrent: " + str(cell.alive))
        print('Alive cells: ' + str(len(aliveCells)))
        if cell.alive == True and 2 <= len(aliveCells) <= 3:
            cell.alive = True
            print('New: ' + str(cell.alive))
        elif cell.alive == False and len(aliveCells) == 3:
            cell.alive = True
            print('New: ' + str(cell.alive))
        else: 
            cell.alive = False
            print('New: ' + str(cell.alive))
        

    def updateCellStatus(self, cell):
        aliveCells = []
        for adjacentCell in self.returnAdjacentCellsAsList(cell):
            if adjacentCell.alive == True:
                aliveCells.append(adjacentCell)
        self.killOrResurrectCell(cell, aliveCells)
        

    def simulateStep(self):
        for row in self.grid.grid:
            for cell in row:
                self.updateCellStatus(cell)


    def playGame(self):
        print("Initial grid: ")
        for line in self.grid.grid:
            lineOfCells = ""
            for cell in line:
                if cell.alive == True:
                    lineOfCells += "O "
                else:
                    lineOfCells += "- "
                # lineOfCells += "(" + str(cell.x) + " " + str(cell.y) + " " + str(cell.alive) + ")"
            print(lineOfCells)
        step = 0
        while step < self.maxSteps:
            step = step + 1
            print("STEP " + str(step))
            self.simulateStep()
            self.printCurrentGridState()
                
        # for line in self.grid.grid:
        #     for cell in line:
        #         print(cell.x,cell.y, cell.alive)
        return self.aliveCells

userInput = [(0,1),(0,0),(1,1),(0,2)]
# userInput = [(0,1),(1,0),(0,0),(2,2),(0,2),(1,1),(2,1)]
game = GamePlayer(4,userInput, 2)
game.playGame()