import GameBoard
import copy
import time

class GameServer():
    def __init__(self, player1, player2, gridSize  = 3):
        self.gameBoard = GameBoard.GameBoard(gridSize)
        self.playerOne = player1
        self.playerTwo = player2
        self.gridSize = gridSize
        self.maxTurn = int(gridSize) * int(gridSize)
        self.currentTurn = 0;
        self.order = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.currentLetter = 0

    def run(self):
        while(True):
            self.currentTurn = 0
            draw = False
            self.gameBoard.reset()
            while(True):
                temp = self.__printGame()
                temp = temp.split("\n")
                for x in temp:
                    print(x)
                    time.sleep(.05)

                player1In = self.__getInput(self.playerOne)
                self.__setPos(x = player1In[0], y = player1In[1], token = -1)

                self.currentTurn = self.currentTurn + 1
                if(self.__checkWin() == True):
                    break
                if(self.__fullBoard() == True):
                    draw = True
                    break

                temp = self.__printGame()
                temp = temp.split("\n")
                for x in temp:
                    print(x)
                    time.sleep(.05)

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

                temp = self.__printGame()
                temp = temp.split("\n")
                for x in temp:
                    print(x)
                    time.sleep(.05)
                self.__charPrint(str(winner) + " is the winner!")
            else:
                temp = self.__printGame()
                temp = temp.split("\n")
                for x in temp:
                    print(x)
                    time.sleep(.05)
                self.__charPrint("No one is the winner! It's a draw")
            while(True):
                good = False
                self.__charPrint("Do you want to play again(Y/N)?")
                self.__charPrint(">>>", endChar="")
                again = input("")
                if (again == "N" or again == "n" or again == "Y" or again == "y"):
                    good = True
                else:
                    good = False
                        
                if(good == True):
                    break
                self.__charPrint("Error: not a vaild input!")

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

    def __getInput(self, player):
        self.__charPrint("It's " + str(player) + " turn.")
        while(True):
            while(True):
                self.__charPrint("please input a letter: ", endChar="")
                inLetter = input("")
                inLetter = inLetter.lower()

                try:
                    ord(inLetter)
                    break
                except TypeError:
                    print("Error: Invaild input!")

            if (ord(inLetter) - 96) <= (int(self.gridSize) * int(self.gridSize)) or (ord(inLetter) - 96) >= 1:
                pos = self.__convertLetter(inLetter)
                inX = pos[0]
                inY = pos[1]

                if (int(inX) <= int(self.gridSize) and int(inX) >= 1):
                    if (int(inY) <= int(self.gridSize) and int(inY) >= 1):
                        if (not(self.__isFull(inX, inY))):
                            break
            self.__charPrint("Error: not a vaild position!")

        return [inX, inY]

    def __getGame(self):
        self.currentLetter = 0
        temp = ""
        self.__clearScreen()
        for x in range(self.gridSize):
            if x !=self.gridSize-1:
                temp = temp + " " + self.__getVisuals(x, "empty") + "  _ "
        temp = temp + "\n"

        for x in range(1, self.gridSize+1):
            temp = temp + self.__getVisualRow(x)
            if x != self.gridSize:
                temp = temp + self.__getLine()

        for x in range(self.gridSize):
            if x !=self.gridSize-1:
                temp = temp + " " + self.__getVisuals(x, "empty") + " |_|"
        temp = temp + "\n"
        
        return temp

    def __convertNum(self, num):
        if num == -1:
            return "x"

        if num == 1:
            return "o"
        
        if num == 0:
            return " "
        
        raise ValueError("Error: num is not a 1, -1, or 0")

    def __convertLetter(self, letter):
        intLetter = ord(letter) - 97
        intLetterX = (intLetter % (int(self.gridSize))) + 1
        intLetterY = 1
        temp = copy.deepcopy(intLetter)

        while (temp != 0):
            if temp % (int(self.gridSize)) == 0:
                intLetterY = intLetterY + 1
            temp = temp - 1

        return[intLetterY, intLetterX]

    def __getVisuals(self, row, type):
        visualX = ["__   __", "\ \_/ /", " \   / ", " / _ \ ", "/_/ \_\\"]
        visualO = [" __  _ ", "/  _  \\", "| | | |", "| |_| |", "\_ _ _/"]
        empty = "       "
        if type == "o":
            return visualO[row]
        elif type == "x":
            return visualX[row]
        elif type == "empty":
            return empty
        else:
            return None

    def __getVisualRow(self, rowNum):
        temp = ""
        row = []
        letters = []
        for y in range(1, self.gridSize+1):
            row.append(str(self.__convertNum(self.__getPos(rowNum, y))))
        
        for j in range(1, self.gridSize+1):
            letters.append(self.order[self.currentLetter])
            self.currentLetter = self.currentLetter + 1

        for r in range(5):
            for x in range(self.gridSize):
                if row[x] == " ":
                    if r != 3:
                        temp = temp + " " + self.__getVisuals(r, "empty") + " "
                    else:
                        temp = temp + "    " + str(letters[x] + "    ")
                elif row[x] == "x":
                    temp = temp + " " + self.__getVisuals(r, "x") + " "
                elif row[x] == "o":
                    temp = temp + " " + self.__getVisuals(r, "o") + " "
                if x != self.gridSize-1:
                    temp = temp + "| |"
            temp = temp + "\n"
        
        return temp
    
    def __getLine(self):
        temp = ""
        for x in range(self.gridSize):
            if x == 0:
                temp = temp + " ________| |"
            elif x == self.gridSize-1:
                temp = temp + "________"
            else:
                temp = temp + "_________| |"

        temp = temp + "\n"

        for x in range(self.gridSize):
            if x == 0:
                temp = temp + "|________   "
            elif x == self.gridSize-1:
                temp = temp + "________|"
            else:
                temp = temp + "_________   "
        temp = temp + "\n"
        return temp

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