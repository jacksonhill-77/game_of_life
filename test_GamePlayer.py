from game_of_life import GamePlayer
from Coordinate import Coordinate

def testInitialisationWorks():
    initialLiveCells = [(1,1),(0,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    assert game.aliveCells[1] == Coordinate(0,1)

# def testOutcomeExpected():
#     initialLiveCells = [(1,1),(0,1),(2,1)]
#     game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
#     aliveCells = game.playGame()
#     expectedOutcome = [()]
#     for cell in aliveCells:
#         assert cell in 
#     assert

def testAliveCellsLiveOrDieCorrectly():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    results = []
    for cell in game.aliveCells:
        print(cell.x,cell.y)
        result = game.doesCellSurvive(cell)
        results.append(result)
    assert results == [False, True, False]

def testDeadCellsLiveOrDieCorrectly():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 1, [0,0], 5,5)
    cell1 = Coordinate(0,0)
    cell2 = Coordinate(1,0)
    assert game.doesCellSurvive(cell1) == False
    assert game.doesCellSurvive(cell2) == True

def testGetAdjacentLiveCoordinates():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    cell = Coordinate(1,1)
    adjacentLiveCoordinates = game.getAdjacentLiveCoordinates(cell)
    cell1 = (adjacentLiveCoordinates[0].x,adjacentLiveCoordinates[0].y)
    cell2 = (adjacentLiveCoordinates[1].x,adjacentLiveCoordinates[1].y)
    assert cell1 == (0,1)
    assert cell2 == (2,1)

    
        
