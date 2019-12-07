import copy

class Grid():
    def __init__(self, gridSize):
        try:
            gridSize = int(gridSize)
        except ValueError:
            raise ValueError("Error: gridSize is not a number!")

        if gridSize <= 1:
            raise ValueError("Error: gridSize must be greater then 1!")


        self.gridSize = gridSize
        self.grid = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]

        self.reset()

    def setPos(self, x, y, value = 0):
        self.__checkInput(x, y)

        self.grid[int(x)-1][int(y)-1] = value

    def getPos(self, x, y):
        self.__checkInput(x, y)

        return copy.deepcopy(self.grid[int(x)-1][int(y)-1])

    def toString(self):
        temp = ""
        for x in range(0, self.gridSize):
            for y in range(0, self.gridSize):
                if y != self.gridSize-1:
                    temp = temp + str(self.grid[x][y]) + "|"
                else:
                    temp = temp + str(self.grid[x][y]) + "\n"
            for i in range(0, self.gridSize):
                if i != self.gridSize-1:
                    temp = temp + "-|"
                else:
                    temp = temp + "-\n"
        return temp

    def reset(self):
        for x in range(0, self.gridSize):
            for y in range(0, self.gridSize):
                self.setPos(x = x+1, y = y+1)

    def __checkInput(self, x, y):
        #---checking for vaild input---
        try:
            x = int(x)
        except ValueError:
            raise ValueError("Error: x is not a number!")

        try:
            y = int(y)
        except ValueError:
            raise ValueError("Error: y is not a number!")


        if x < 1 or x > self.gridSize:
            raise ValueError("Error: x is outside the grid!")

        if y < 1 or y > self.gridSize:
            raise ValueError("Error: y is outside the grid!")
        #---vaild input check done---

if __name__ == "__main__":
    raise RuntimeError("Error: Must use this class as a dependent!")