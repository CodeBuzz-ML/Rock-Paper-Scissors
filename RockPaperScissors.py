"""
Project: - Rock, Paper, Scissor with Adhyayan
Authors: - CodeBuzz, SimulatorWinner
Language: - Python 3.11.0

"""
from random import *

while 0>-1:
  str_user_choice = input("Enter your Selection:- ")
  if (str_user_choice.lower() == "rock"):
    user_choice = 0
  elif (str_user_choice.lower() == "paper"):
    user_choice = 1
  elif (str_user_choice.lower() == "scissors"):
    user_choice = 2
  elif (str_user_choice.lower() != "rock" or str_user_choice.lower() != "choice" or str_user_choice.lower() != "scissor"):
    print("Incorrect Choice!")
    exit()

  computer_choice = randint(0,2) #randint(start,end)
  #0 = Rock
  #1 = Paper
  #2 = Scissor
  
  if (computer_choice == 0):
    if (user_choice == 0):
      print("Draw (Computer chose Rock)") # Rock vs Rock
    if (user_choice == 1):
      print("You win") # Rock vs Paper
    if (user_choice == 2):
      print("Computer Won") # Rock vs Scissors
      
  elif (computer_choice == 1):
    if (user_choice == 0): # Paper vs Rock
      print("Computer Won")
    if (user_choice == 1):
      print("Draw (Computer chose paper)") # Paper vs Paper
    if (user_choice == 2):
      print("You won") # Paper vs Rock
  elif (computer_choice == 2):
    
    if (user_choice == 0):
      print("You won") # Sciscors vs Rock
    if (user_choice == 1):
      print("Computer Won") # Scissors vs Paper
    if (user_choice == 2):
      print("Draw (Computer chose scissors)") # Scissors vs Scissors