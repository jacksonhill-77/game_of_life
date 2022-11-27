from game_of_life import GamePlayer
from Coordinate import Coordinate

def testInitialisationWorks():
    initialLiveCells = [(1,1),(0,1),(2,1)]
    game = GamePlayer(initialLiveCells, 5, [0,0], 5,5)
    assert game.aliveCells[1] == Coordinate(0,1)
        
