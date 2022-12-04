from game_of_life import GamePlayer
from Cell import Cell

def testInitialisationWorks():
    initialLiveCells = [(1,1),(0,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    assert game.aliveCells[1] == Cell(0,1)

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
    cell1 = Cell(0,0)
    cell2 = Cell(1,0)
    assert game.doesCellSurvive(cell1) == False
    assert game.doesCellSurvive(cell2) == True

def testGetAdjacentLiveCells():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    cell = Cell(1,1)
    adjacentLiveCells = game.getAdjacentLiveCells(cell)
    cell1 = (adjacentLiveCells[0].x,adjacentLiveCells[0].y)
    cell2 = (adjacentLiveCells[1].x,adjacentLiveCells[1].y)
    for cell in adjacentLiveCells:
        print(cell.x,cell.y)
    assert cell1 == (0,1)
    assert cell2 == (2,1)

def testDetermineIfEachCellLivesOrDies():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    cellsWeNeedToLookAt = [Cell(0,1),Cell(1,1)]
    cellsThatSurvive = game.determineIfEachCellSurvives(cellsWeNeedToLookAt)
    assert cellsThatSurvive == [Cell(1,1)]

def testFindAllCellsToLookAt():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    cellsWeNeedToLookAt = game.findAllCellsToLookAt()
    sampleCells = [Cell(0,1),Cell(3,2),Cell(0,2)]
    for cell in sampleCells: 
        assert cell in cellsWeNeedToLookAt
    assert len(cellsWeNeedToLookAt) == 15

def testOutcomeIsCorrect():
    initialLiveCells = [(0,1),(1,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    result = game.playGame()

# def testOutcomeIsCorrectIfOriginIsNegative():


    
        
