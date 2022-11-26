class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getAdjacentCoordinates(coordinates):
        adjacentCoordinates = set()
        for coordinate in coordinates:
            for x in range(coordinate.x - 1, 2):
                for y in range (coordinate.y - 1, 2):
                    adjacentCoordinates.add(Coordinate(x, y))
        return adjacentCoordinates