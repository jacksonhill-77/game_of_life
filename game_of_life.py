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

class Cell:

    def __init__(self, x, y):
        self.alive = False
        self.x = x
        self.y = y

class Grid:

    def __init__(self, gridSize, initialLiveCells):
        self.gridSize = gridSize
        self.grid = []

        for x in range(gridSize):
            cellList = []
            for y in range(gridSize):
                cell = Cell(x, y)
                cellList.append(cell)
            self.grid.append(cellList)

class GamePlayer:

    def __init__(self, gridSize, initialLiveCells, steps):
        self.grid = Grid(gridSize, initialLiveCells)
        self.initialLiveCells = initialLiveCells
        self.steps = steps
        self.currentLiveCells = []

    def checkAdjacentCellStatus(self):
        for cell in self.grid.cells:
            adjacentLiveCells = []
            # for gridCell in self.grid:
            #     if gridCell.x == cell.x:
            #     gridCell.x == cell.x - 1 or gridCell.x == cell.x + 1:

    def playGame(self):
        for line in self.grid.grid:
            for cell in line:
                print(cell.x,cell.y)
        return self.currentLiveCells

userInput = [(0,1),(2,4),(6,5),(6,6),(9,2)]
game = GamePlayer(10,userInput, 10)
game.playGame()