
def gameLoop():
    while True:
        gameState = gameMenu()
        if gameState == 1:
            print("Starting a new game...")
            newGame()
        
        elif gameState == 2:

            print("Exiting the game. Goodbye!")
            exitGame()
            break        


def gameMenu():
    print("Welcome to the Game Menu!")
    print("1. start a game")
    print("2. exit the game")

    gameState = int(input("What we do you want to do?"))
    return gameState


#BUILDING NEW GAME FUNCTIONS 
def newGame():

    playerHealth = 5
    enemyHealth = 5
    print("You have a dice")
    print("You can roll the dice by typing 'roll' or exit the game by typing 'exit'")
    while playerHealth > 0 and enemyHealth > 0:
        playerInput = input("What do you want to do? (roll/exit):")
        if playerInput.lower() == "roll":
            playerRoll = diceRoll()
            enemyRoll = diceRoll()
            print(f"You rolled a {playerRoll}")
            print(f"The enemy rolled a {enemyRoll}")

            if playerRoll > enemyRoll:
                enemyHealth -= 1
                print(f"You hit the enemy! Enemy health is now {enemyHealth}")
            elif playerRoll < enemyRoll:
                playerHealth -= 1
                print(f"The enemy hit you! Your health is now {playerHealth}")

def diceRoll():
    import random
    return random.randint(1,6)

def exitGame():
    print("Thank you for playing! Exiting the game...")
    

#CALLING GAME LOOP FUNCTION
gameLoop()