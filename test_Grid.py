from game_of_life import Grid

def testGridCoordinates():
    userInput = [(0,1),(2,4),(6,5),(6,6),(9,2)]
    grid = Grid(10,userInput)
    for i in grid.grid:
        for x in i:
            print(x.alive)
    assert grid.grid[0][3].x == 0
    assert grid.grid[0][3].y == 3

def testInitialAliveCellsAreAlive():
    userInput = [(0,1),(2,4),(6,5),(6,6),(9,2)]
    grid = Grid(10,userInput)
    assert grid.grid[0][3].alive == False
    assert grid.grid[2][4].alive == True