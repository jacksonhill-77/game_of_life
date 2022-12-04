from GamePlayer import GamePlayer

class Interface:
    def __init__(self):
        self.initialLiveCells = input("Please enter the coordinates of the initial live cells as a list of tuple, or press ENTER for the default [(1,1),(0,1),(2,1)]:")
        if len(self.initialLiveCells) == 0:
            self.initialLiveCells = [(1,1),(0,1),(2,1)]
        self.maxSteps = input("Please enter the amount of steps the game should run for, or press ENTER for the default (5)")
        if len(self.maxSteps) == 0:
            self.maxSteps = 5
        self.gridOrigin = input("Please enter the coordinate of the top left corner of the grid to view the output on, or press ENTER for the default (0,0):")
        if len(self.gridOrigin) == 0:
            self.gridOrigin = (0,0)
        self.gridX = input("Please enter the X dimension of the viewing grid, or press ENTER for the default (5):") 
        if len(self.gridX) == 0:
            self.gridX = 5
        self.gridY = input("Please enter the Y dimension of the viewing grid, or press ENTER for the default (5):") 
        if len(self.gridY) == 0:
            self.gridY = 5

    def runGame(self):
        game = GamePlayer(self.initialLiveCells,self.maxSteps,self.gridOrigin,self.gridX,self.gridY)
        print(game)

