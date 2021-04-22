import random, time
# guessing game

# RPS

# Dice Roll

# Fortune Teller

def guessingGame():
  print("This is the guessing game")

def RPS():
  # print("This is rock paper scissors")

  # cpu and player
  # cpu chooses a random number between 1 - 3
  # get player choice
  # use nested condiditionals
  print("1. Rock \n"
  "2. Paper\n"
  "3. Scissors\n")
  userInput = int(input("Please choose your class: "))
  cpu = random.randint(1,3)
  if(userInput == cpu):
    print("Tie game")
  elif(userInput != cpu):
    if(userInput == 1):
      if(cpu == 2):
        print("You lose I chose Paper!")
      elif(cpu == 3):
        print("You win I chose scissors")
    if(userInput == 2):
      if(cpu == 1):
        print("You win I chose Rock!")
      elif(cpu == 3):
        print("You lose I chose scissors")
    if(userInput == 3):
      if(cpu == 1):
        print("You lose I chose Rock!")
      elif(cpu == 2):
        print("You win I chose Paper") 

    

def diceRoll():
  # print("This is the dice roll")
  diceNumber = random.randint(1,6)
  print("You got a " + str(diceNumber))


def fortuneTeller():
  # print("This is the fortune teller")
  # using a list, add 5 fourtunes and randomly choose one to output the user
  fortuneList = ["You suck at video games", "You will play a free admin game in the next 1 hour", "You are now a pro", "am pro", "sup", " ", "ha rekt noob you wasted your time"]
  print(fortuneList[random.randint(0, (len(fortuneList) - 1))])

# Main Function
# this is where we defind how we want our program to run
def main():
  # print("This is the main function")
  # tell the user their game options
  # ask the user to choose one
  # call the correct function based on the user input
  print("1. Guessing Game")
  print("2. Rock Paper Scissors")
  print("3. Dice Roll")
  print("4. Fortune Teller")
  userInput = input("which game whould you like to play? Please specify with a number: ")
  # 1 != "1"

  if(userInput == "1"):
    guessingGame()
  elif(userInput == "2"):
    RPS()
  elif(userInput == "3"):
    diceRoll() 
  elif(userInput == "4"):
    fortuneTeller() 
  else:
    print("Sorry that was a invalid input")
    main()

# This controls the execution of our code
if __name__ == "__main__":
  main()