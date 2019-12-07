import Game

print("How big do you want to grid? (must be >= 2)")
while(True):
    gridSize = input(">>>")
    try:
        int(gridSize)
        if(int(gridSize) > 1):
            break
    except ValueError:
        pass
    print("Error: not a vaild input!")


print("What is your name player 1?")
player1 = input(">>>")

print("What is your name player 2?")
player2 = input(">>>")

game = Game.Game(player1 = player1, player2 = player2, gridSize = int(gridSize))
game.run()