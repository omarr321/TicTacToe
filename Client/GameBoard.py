import Grid

class GameBoard():
    def __init__(self, gridSize = 3):
        self.grid = Grid.Grid(gridSize = gridSize)
    
    def getPos(self, x, y):
        return self.grid.getPos(x, y)

    def setPos(self, x, y, token):
        if token != -1 and token != 1:
            raise ValueError("Error: token must be -1 or 1")
        return self.grid.setPos(x, y, token)

    def reset(self):
        self.grid.reset()
    
    def toString(self):
        return self.grid.toString()

if __name__ == "__main__":
    raise RuntimeError("Error: Must use this class as a dependent!")