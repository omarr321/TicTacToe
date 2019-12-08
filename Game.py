import GameBoard
import copy

class Game():
    def __init__(self, player1, player2, gridSize  = 3):
        self.gameBoard = GameBoard.GameBoard(gridSize)
        self.playerOne = player1
        self.playerTwo = player2
        self.gridSize = gridSize
        self.maxTurn = int(gridSize) * int(gridSize)
        self.currentTurn = 0;

    def run(self):
        while(True):
            self.currentTurn = 0
            draw = False
            self.gameBoard.reset()
            while(True):
                print(self.__printGame())
                player1In = self.__getInput(self.playerOne)
                self.__setPos(x = player1In[0], y = player1In[1], token = -1)

                self.currentTurn = self.currentTurn + 1
                if(self.__checkWin() == True):
                    break
                if(self.__fullBoard() == True):
                    draw = True
                    break


                print(self.__printGame())
                player2In = self.__getInput(self.playerTwo)
                self.__setPos(x = player2In[0], y = player2In[1], token = 1)

                self.currentTurn = self.currentTurn + 1
                if(self.__checkWin() == True):
                    break
                if(self.__fullBoard() == True):
                    draw = True
                    break
            
            if draw == False:
                winner = self.__getWinner()

                print(self.__printGame())
                print(str(winner) + " is the winner!")
            else:
                print(self.__printGame())
                print("No one is the winner! It's a draw")
            while(True):
                good = False
                print("Do you want to play again(Y/N)?")
                again = input(">>>")
                if (again == "N" or again == "n" or again == "Y" or again == "y"):
                    good = True
                else:
                    good = False
                        
                if(good == True):
                    break
                print("Error: not a vaild input!")

            if(again == "N" or again == "n"):
                break

    def __setPos(self, x, y, token):
        try:
            self.gameBoard.setPos(x, y, token)
        except ValueError:
            return  False
        return True

    def __getPos(self, x, y):
        return self.gameBoard.getPos(x, y)

    def __checkWin(self):
        for i in range(1, self.gridSize+1):
            total = 0
            for j in range(1, self.gridSize+1):
                total += self.gameBoard.getPos(i, j)
            if total == int(self.gridSize) * -1:
                return True
            if total == int(self.gridSize) * 1:
                return True

            total = 0
            for k in range(1, self.gridSize+1):
                total += self.gameBoard.getPos(k, i)
            if total == int(self.gridSize) * -1:
                return True
            if total == int(self.gridSize) * 1:
                return True

        total = 0
        for i in range(1, self.gridSize+1):
            total += self.gameBoard.getPos(i, i)
        if total == int(self.gridSize) * -1:
            return True
        if total == int(self.gridSize) * 1:
            return True

        total = 0
        for i in range(1, self.gridSize+1):
            total += self.gameBoard.getPos(i, self.gridSize+1-i)
        if total == int(self.gridSize) * -1:
                return True
        if total == int(self.gridSize) * 1:
            return True

        return False

    def __getWinner(self):
        for i in range(1, self.gridSize+1):
            total = 0
            for j in range(1, self.gridSize+1):
                total += self.gameBoard.getPos(i, j)
            if total == int(self.gridSize) * -1:
                return str(self.playerOne)
            if total == int(self.gridSize) * 1:
                return str(self.playerTwo)

            total = 0
            for k in range(1, self.gridSize+1):
                total += self.gameBoard.getPos(k, i)
            if total == int(self.gridSize) * -1:
                return str(self.playerOne)
            if total == int(self.gridSize) * 1:
                return str(self.playerTwo)

        total = 0
        for i in range(1, self.gridSize+1):
            total += self.gameBoard.getPos(i, i)
        if total == int(self.gridSize) * -1:
                return str(self.playerOne)
        if total == int(self.gridSize) * 1:
            return str(self.playerTwo)

        total = 0
        for i in range(1, self.gridSize+1):
            total += self.gameBoard.getPos(i, self.gridSize+1-i)
        if total == int(self.gridSize) * -1:
                return str(self.playerOne)
        if total == int(self.gridSize) * 1:
            return str(self.playerTwo)

        return None

    def __printGame(self):
        temp = ""
        temp = temp + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        for x in range(1, self.gridSize+1):
            for y in range(1, self.gridSize+1):
                if y != self.gridSize:
                    temp = temp + str(self.__convertNum(self.__getPos(y, x))) + "|"
                else:
                    temp = temp + str(self.__convertNum(self.__getPos(y, x))) + "\n"
            if x != self.gridSize:        
                for i in range(1, self.gridSize+1):
                    if i != self.gridSize:
                        temp = temp + "-|"
                    else:
                        temp = temp + "-\n"
        return temp

    def __convertNum(self, num):
        if num == -1:
            return "x"

        if num == 1:
            return "o"
        
        if num == 0:
            return " "
        
        raise ValueError("Error: num is not a 1, -1, or 0")

    def __getInput(self, player):
        print("It is " + str(player) + " turn.")
        while(True):
            inX = input("please input a x position: ")
            inY = input("please input a y position: ")
            if (int(inX) <= int(self.gridSize) and int(inX) >= 1):
                if (int(inY) <= int(self.gridSize) and int(inY) >= 1):
                    if (not(self.__isFull(inX, inY))):
                        break
            print("Error: not a vaild position!")

        return [inX, inY]
    
    def __isFull(self, x, y):
        if str(self.gameBoard.getPos(x, y)) != "0":
            return True  
        return False
    
    def __fullBoard(self):
        if self.maxTurn == self.currentTurn:
            return True
        else:
            return False

if __name__ == "__main__":
    raise RuntimeError("Error: Must use this class as a dependent!")