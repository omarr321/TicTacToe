import GameServer
import threading
import time

class Lobby():
    def __init__(self):
        self.__lobbyList3x3 = []
        self.__lobbyList4x4 = []
        self.__lobbyList5x5 = []

    def checkForPlayer(self, player):
        for x in self.__lobbyList3x3:
            if player == x:
                return True

        for x in self.__lobbyList4x4:
            if player == x:
                return True

        for x in self.__lobbyList5x5:
            if player == x:
                return True
        
        return False

    def addPlayer(self, player, gridSize):
        if gridSize == 3:
            self.__lobbyList3x3.append(player)
        elif gridSize == 4:
            self.__lobbyList4x4.append(player)
        elif gridSize == 5:
            self.__lobbyList5x5.append(player)
        else:
            raise ValueError ("Error: grid size is not 3,4, or 5!")

    def removePlayer(self, player, gridSize):
        if gridSize == 3:
            self.__lobbyList3x3.remove(player)
        elif gridSize == 4:
            self.__lobbyrList4x4.remove(player)
        elif gridSize == 5:
            self.__lobbyList5x5.remove(player)
        else:
            raise ValueError ("Error: grid size is not 3,4, or 5!")

    def __checkLobby(self, gridSize):
        print("\n\nchecking Lobby...")
        if gridSize == 3:
            print("lobby 3x3:")
            print("[", end = "")
            for x in self.__lobbyList3x3:
                print("(" + str(x[2]) + " " + str(x[1]) + ")", end = ", ")
            print("]")
            if(self.__lobbyList3x3.__len__() >= 2):
                print("Lobby 3x3 has enough players; creating game...")
                return True
            return False
        elif gridSize == 4:
            print("lobby 4x4:")
            print("[", end = "")
            for x in self.__lobbyList4x4:
                print(x[2], end = ", ")
            print("]")
            if(self.__lobbyList4x4.__len__() >= 2):
                print("Lobby 4x4 has enough players; creating game...")
                return True
            return False
        elif gridSize == 5:
            print("lobby 5x5:")
            print("[", end = "")
            for x in self.__lobbyList5x5:
                print(x[2], end = ", ")
            print("]")
            if(self.__lobbyList5x5.__len__() >= 2):
                print("Lobby 5x5 has enough players; creating game...")
                return True
            return False
        else:
            return False


    def run(self):
        while(True):
            if(self.__checkLobby(3)):
                newGame = GameServer.GameServer(self.__lobbyList3x3.pop(), self.__lobbyList3x3.pop(), 3)
                game = threading.Thread(target=newGame.run)
                game.start()
                print("Done!")
                pass
            else:
                print("Lobby 3x3 still has room")

            if(self.__checkLobby(4)):
                newGame = GameServer.GameServer(self.__lobbyList4x4.pop(), self.__lobbyList4x4.pop(), 4)
                game = threading.Thread(target=newGame.run)
                game.start()
                print("Done!")
                pass
            else:
                print("Lobby 4x4 still has room")

            if(self.__checkLobby(5)):
                newGame = GameServer.GameServer(self.__lobbyList5x5.pop(), self.__lobbyList5x5.pop(), 5)
                game = threading.Thread(target=newGame.run)
                game.start()
                print("Done!")
                pass
            else:
                print("Lobby 5x5 still has room")
            
            print("--------------------------------------------------------------------------------------------------------------")
            time.sleep(5)
    
    if __name__ == "__main__":
        raise RuntimeError("Error: Must use this class as a dependent!")