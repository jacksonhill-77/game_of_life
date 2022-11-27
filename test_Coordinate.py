from Coordinate import Coordinate

def testGetAdjacentCellsWorks():
    coordinate = Coordinate(5,5)
    adjacentCells = coordinate.getAdjacentCoordinates()
    expectedAdjacentCells = [(4,4),(5,4),(6,4),(4,5),(5,5),(6,5),(4,6),(5,6),(6,6)]
    assert expectedAdjacentCells in adjacentCells == True