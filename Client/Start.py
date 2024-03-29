import GameLocally
import time
import sys
from socket import *

def __charPrint(string, endChar = "\n", timePerChar = .04):
    for x in string:
        print(x, end="", flush=True)
        time.sleep(timePerChar)
    print("", end=endChar)

def __clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while(True):
    __clearScreen()
    __charPrint("Welcome to")
    time.sleep(1)
    print(" _ ___  ____   _     __ _ _            ___ _____ _             __ _ _            ____ _  ___")
    time.sleep(.2)
    print("|___    __ _| |_|  / _ _ __|          |____   _ __| _ _ _    / _ ____|          |___    __ _| ___  _    _ ___")
    time.sleep(.2)
    print("     | |       _  | |         _ _ __       | |     |___  |  | |          ___ _       | |     /   _  \  /  _  \\")
    time.sleep(.2)
    print("     | |      | | | |        |__ __ |      | |     /  _  |  | |        |_ _ __|      | |     | |  | |  | |_| |")
    time.sleep(.2)
    print("     | |      | | | |_ _ __                | |     | |_| |  | |_ __ _                | |     | |__| |  |  ___|")
    time.sleep(.2)
    print("     |_|      |_|  \___ _ _|               |_|     \__  _|   \____ __|               |_|     \__ _ _/  \ __ _|")
    time.sleep(1)
    print("\n")

    while (True):
        __charPrint("What Would you like to do?")
        __charPrint("1|Play Online")
        __charPrint("2|Play Locally")
        __charPrint("3|Credits")
        __charPrint("4|Quit")
        __charPrint(">>>", endChar="")
        userIn = input("")

        try:
            userIn = int(userIn)
            if (userIn >= 1 and userIn <= 4):
                break
            __charPrint("Error: Invaild input!", endChar="")
            time.sleep(2)
        except ValueError:
            __charPrint("Error: Invaild input!", endChar="")
            time.sleep(2)
        print("\n")

    __clearScreen()

    if userIn == 1:
        grid = 0
        #__charPrint("Error: online functionality not implemented!")
        #__charPrint("Returning to Main Menu...", endChar="")
        #time.sleep(2)
        __charPrint("What is your name?")
        __charPrint(">>>", endChar="")
        name = input("")

        while(True):
            __charPrint("Pick a difficulty:")
            __charPrint("1|Normal  (3x3)")
            __charPrint("2|Hard    (4x4)")
            __charPrint("3|Extreme (5x5)")
            __charPrint(">>>", endChar="")
            userIn = input("")
            try:
                userIn = int(userIn)
                if(userIn >= 1 and userIn <= 3):

                    grid = userIn + 2
                    break
            except ValueError:
                pass
            __charPrint("Error: not a vaild input!", endChar="")
            time.sleep(2)
            print("\n")

        __charPrint("establishing connection to server...", endChar="")
        temp = 1
        connected = False
        while(True):
            try:
                clientSocket = socket(AF_INET, SOCK_STREAM)
                clientSocket.connect(("10.0.0.18", 25535))
                connected = True
                break
            except ConnectionRefusedError:
                __charPrint("\nTried " + str(temp) + " time(s)...", endChar="")
                if (temp != 5):
                    temp = temp + 1
                else:
                    __charPrint("\nCan not connect to server")
                    __charPrint("going back to Main Menu...")
                    time.sleep(2)
                    break
        
        if connected == True:
            print("")
            message = clientSocket.recv(1024)
            message = clientSocket.recv(1024)
            clientSocket.send(name.encode())
            message = clientSocket.recv(1024)
            clientSocket.send(str(grid).encode())
            __clearScreen()
            __charPrint("Waiting for opponent", endChar="")

            time.sleep(1)
            while(True):
                message = clientSocket.recv(1024).decode()
                if (message == "alive?"):
                    clientSocket.send("yup".encode())
                    print(".", end="", flush=True)
                else:
                    break

            while(True):
                print("would be in game!")

    elif userIn == 2:
        while(True):
            __charPrint("Pick a difficulty:")
            __charPrint("1|Normal  (3x3)")
            __charPrint("2|Hard    (4x4)")
            __charPrint("3|Extreme (5x5)")
            __charPrint(">>>", endChar="")
            userIn = input("")
            try:
                userIn = int(userIn)
                if(userIn >= 1 and userIn <= 3):
                    break
            except ValueError:
                pass
            __charPrint("Error: not a vaild input!", endChar="")
            time.sleep(2)
            print("\n")

        if userIn == 1:
            gridSize = 3
        elif userIn == 2:
            gridSize = 4
        else:
            gridSize = 5

        print ("")

        __charPrint("What is your name player 1?")
        __charPrint(">>>", endChar="")
        player1 = input("")

        print("")

        __charPrint("What is your name player 2?")
        __charPrint(">>>", endChar="")
        player2 = input("")

        game = GameLocally.GameLocally(player1 = player1, player2 = player2, gridSize = gridSize)
        game.run()

    elif userIn == 3:
        __charPrint("Game made by Omar Radwan", endChar="")
        time.sleep(2)
        print("\n\n")

        while(True):
            __charPrint("What Would you like to do?")
            __charPrint("1|Back")
            __charPrint("2|Quit")
            __charPrint(">>>", endChar="")
            userIn = input("")
            
            try:
                userIn = int(userIn)
                if (userIn >= 1 and userIn <= 2):
                    break
                __charPrint("Error: Invaild input!", endChar="")
                time.sleep(2)
                print("\n")
            except ValueError:
                __charPrint("Error: Invaild input!", endChar="")
                time.sleep(2)
                print("\n")
            
        if userIn == 2:
            __clearScreen()
            __charPrint("Good Bye!", endChar="")
            time.sleep(2)
            sys.exit(0)

    elif userIn == 4:
        __charPrint("Good Bye!", endChar="")
        time.sleep(2)
        sys.exit(0)
        
    else:
        print("A Critical Error Has Occurred")
        print("Shuting Down...")
        sys.exit(1)

if __name__ != "__main__":
    raise RuntimeError("Error: Can not use this class as a dependent!")