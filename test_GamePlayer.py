from game_of_life import GamePlayer, Cell, Grid

def testAdjacentCellsPickedCorrectly():
    userInput = [(0,0),(0,1),(1,1),(0,2)]
    cell = Cell(2,1)
    cellsX = []
    cellsY = []
    cellsAlive = []
    game = GamePlayer(4,userInput, 1)

    listOfAdjacentCells = game.returnAdjacentCellsAsList(cell, game.grid.grid)
    for cell in listOfAdjacentCells:
        cellsX.append(cell.x)
        cellsY.append(cell.y)
        cellsAlive.append(cell.alive)
    assert cellsX == [1,2,3,1,3,1,2,3]
    assert cellsY == [0,0,0,1,1,2,2,2]
    assert cellsAlive == [False,False,False,True,False,False,False,False]

# def testCorrectCellsAreDeadOrAlive():
#     userInput = [(0,0),(0,1),(1,1),(0,2)]
#     game = GamePlayer(4,userInput, 1)
#     game.playGame()
#     assert game.grid.grid[3][2].alive == False
#     assert game.grid.grid[4][4].alive == False
#     assert game.grid.grid[1][0].alive == True
#     assert game.grid.grid[1][2].alive == True