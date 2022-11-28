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

def testDoesCellSurvive():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    results = []
    for cell in game.aliveCells:
        print(cell.x,cell.y)
        result = game.doesCellSurvive(cell)
        results.append(result)
    assert results == [False, True, False]
    
        
