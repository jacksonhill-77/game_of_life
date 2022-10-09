from game_of_life import GamePlayer

def cellParametersToTuple(cell):
    return (cell.x,cell.y,cell.alive)

def testCorrectCellsAreDeadOrAlive():
    userInput = [(0,1),(1,0),(0,0),(2,2),(0,2),(1,1),(2,1)]
    game = GamePlayer(4,userInput, 1)
    game.playGame()
    finalCells = []
    assert game.grid.grid[3][2].alive == False

testCorrectCellsAreDeadOrAlive()