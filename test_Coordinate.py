from Coordinate import Coordinate

def convertCoordinatesToTuples(listOfCoordinates):
    tupleList = []
    for coordinate in listOfCoordinates:
        tupleList.append((coordinate.x,coordinate.y))
    return tupleList

def testGetAdjacentCellsWorks():
    coordinate = Coordinate(5,5)
    adjacentCells = coordinate.getAdjacentCoordinates()
    adjacentCells = convertCoordinatesToTuples(adjacentCells)
    expectedAdjacentCells = [(4,4),(5,4),(6,4),(4,5),(6,5),(4,6),(5,6),(6,6)]
    assert len(set(adjacentCells + expectedAdjacentCells)) == 8

