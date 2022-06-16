import random

class Player(): # This is the player class, we use this to track stats across multiple games.
  def __init__(self, name):
    self.__name = name # Player name

    # These 3 variables track the player's win-loss record
    self.__wins = 0
    self.__losses = 0
    self.__ties = 0

    # These 3 variables track how many times the player uses each move
    self.__rockCounter = 0
    self.__paperCounter = 0
    self.__scissorsCounter = 0

  # This function increments the win-loss counter appropriately
  def keepScore(self, result): # Result is passed into this function as an integer
    if result == 0:
      self.__losses += 1
    elif result == 1:
      self.__wins += 1
    elif result == 2:
      self.__ties += 1
    else:
      return

  # This function tracks the amount of times the player chooses each move
  def moveCounter(self, move): # The move choice is passed as a string, and the counters are incremented as a result.
    if move == "rock":
      self.__rockCounter += 1
    elif move == "paper":
      self.__paperCounter += 1
    else: self.__scissorsCounter += 1

  # This function prints the scoreboard and the counters.
  def showRecords(self):
    print("Wins: {0} | Losses: {1} | Ties {2}".format(self.__wins, self.__losses, self.__ties))
    print(f"You have used Rock {self.__rockCounter} times, Paper {self.__paperCounter} times, and Scissors {self.__scissorsCounter} times.")

  # This function is used to get the player name since it's a private variable.
  def getName(self):
    return self.__name

# This is just to clean up the code a little bit, all this does is prompt the user and take input.
def userPrompt():
  userMove = input("Enter r for rock, p for paper, s for scissors, or v to view records: \n").lower()
  return userMove

def getUserMove(player):
  move = userPrompt() # I got sick of copy-pasting this so I made the prompt its own function.

  # This dictionary checks if the user input is valid and will change the input into the proper move.
  decisions = { 
    "r": "rock",
    "p": "paper",
    "s": "scissors",
  }

  # This checks if the user wants to see their records first, and then prompts to play their hand.
  while move == "v":
    player.showRecords()
    move = userPrompt()

  # This checks if the input is not valid, and will continue looping until the user figures it out.
  while move not in decisions:
    print ("Invalid input.")
    move = userPrompt()

  move = decisions[move] # This takes the input the user put in and finds the key-value pair and changes it to the move that corresponds to the letter.
  
  player.moveCounter(move) # This calls the move counter function.
  return move # This returns the string, this should only output [rock, paper, scissors]

# This generates the CPU's move.
def getCompMove():
  return random.choice(["rock", "paper", "scissors"])  #  CPU will choose randomly one of three moves from this list.

# This handles all the logic for RPS, who wins, who loses, ties, etc...
# Both moves are sent here, and so is the player object we're creating.
# The player object will get their stat functions called in this function.
def gameLogic(userMove, compMove, player): 

  # This dictionary tracks which move beats what. 
  winConditions = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
    }

  # This simply prints the player's name and what moves each player chose.
  print(player.getName() + " chose {0}, and the CPU chose {1}.".format(userMove, compMove))

  # This is where the game logic is handled
  # This first checks if the moves are the same, and increments the tie counter if so.
  # Then it checks if the user's move beats the CPU's move, then increments wins counter.
  # Finally if neither condition is true it assumes CPU wins and increments losses counter.
  if userMove == compMove:
    print ("Both players chose {0}! It's a tie!".format(userMove))
    player.keepScore(2)
  elif userMove in winConditions[compMove]:
    print ("{0} beats {1}! You win!".format(userMove, compMove))
    player.keepScore(1)
  else:
    print ("{0} beats {1}! CPU wins!".format(compMove, userMove))  
    player.keepScore(0)

# This is where the magic happens.

# This prompts the player to enter their name.
print("Time to play some Rock Paper Scissors!")
name = input("Enter your name here: ")
player = Player(name)

# This loop calls the functions, and the player will keep playing as long as they want to.
while True:
  userMove = getUserMove(player)
  compMove = getCompMove()
  gameLogic(userMove, compMove, player)

  playAgain = input("Do you want to play again? (y)\n")
  if playAgain.lower() != "y":
    break


