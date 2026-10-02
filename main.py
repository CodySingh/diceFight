


def gameLoop():
    while True:
        gameState = gameMenu()
        if gameState == 1:
            print("Starting a new game...")
            newGame()
        
        if gameState == 2:
            print("Loading a game...")
            loadGame()
        
        elif gameState == 3:

            print("Exiting the game. Goodbye!")
            exitGame()
            break


def gameMenu():
    print("Welcome to the Game Menu!")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Exit")

    gameState = int(input("What we do you want to do?"))
    return gameState


def newGame():
    print("newGame function is called")



def loadGame():
    print("loadGame function is called")


def exitGame():
    print("exitGame function is called")


gameLoop()