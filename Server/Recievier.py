import socket
import threading
import time
import Lobby

#---------------------------
HOST = ""
PORT = 25535
#---------------------------
lobby = Lobby.Lobby()

class Receiver():
    def __init__(self, host, port, lobby):
        self.__lobby = lobby

        self.__serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__serverSocket.bind((host, port))

        newLobby = threading.Thread(target=lobby.run)
        
        print("The server is ready to receive...")
        newLobby.start()
    
    def listen(self):
        self.__serverSocket.listen(3)
        while(True):
            client, addr = self.__serverSocket.accept()
            newThread = threading.Thread(target = self.ClientController,args = (client, addr))
            newThread.start()


    def ClientController(self, client, addr):
        client.send("200 ok".encode())
        client.send("What is the name you want players to refer to you by?".encode())
        name = client.recv(1024).decode()

        client.send("What gridSize?".encode())
        gridSize = int(client.recv(1024).decode())

        player = [client, addr, name]

        if gridSize == 3:
            self.__lobby.addPlayer(player, 3)
        elif gridSize == 4:
            self.__lobby.addPlayer(player, 4)
        elif gridSize == 5:
            self.__lobby.addPlayer(player, 5)

        time.sleep(1)
        temp = 0

        if self.__lobby.checkForPlayer(player) == True:  
            print(str(player[2]) + " is in the lobby!")
            
        while(self.__lobby.checkForPlayer(player) == True):
            try:
                if temp == 5:
                    print(str(player[2]) + " is in the lobby!")
                    temp = 0
                client.send("alive?".encode())
                client.recv(1024)
                temp = temp + 1
                time.sleep(1)
            except ConnectionResetError:
                print(str(player[2]) + " has left the lobby!")

                if gridSize == 3:
                    self.__lobby.removePlayer(player, 3)
                elif gridSize == 4:
                    self.__lobby.removePlayer(player, 4)
                elif gridSize == 5:
                    self.__lobby.removePlayer(player, 5)



        

temp = Receiver(HOST, PORT, lobby)
temp.listen()

if __name__ != "__main__":
    raise RuntimeError("Error: Can not use this class as a dependent!")