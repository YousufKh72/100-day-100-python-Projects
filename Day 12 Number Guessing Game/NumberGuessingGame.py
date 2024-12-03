#Number Guessing Game Objectives:
from art import Logo
from random import randint
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# HINT: Use clear() to clear the console output.

def difficulty(): 
  choice = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
  """Checks the difficulty of the game to return how many attempts the player gets."""
  if choice == "easy":
    return 15
  elif choice == "medium":
    return 10
  elif choice == "hard":
    return 5
  else :
    print("You have chosen wrong.")
    return 0
  
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 

def compare(og_number, turns):
  return

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def guessNumber():
  consent = input("Do you want to play a game?\n Type 'y' for yes or 'n' for no: ")
  if consent == "n":
    return
  else: 
    clear()
    number = randint(1, 100)
    print(Logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # print(number)
    remaining_attempts = difficulty()
    # print(f"Psst!, the number is {number}")
    while remaining_attempts >= 0:
      if remaining_attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The number was : {number}")
        break
      print(f"You have {remaining_attempts} attempts remaining to guess the number.")
      try:
        player_guess = int(input("Make a guess: "))
      except ValueError:
        print("Please enter a valid integer.")
        continue
      if player_guess == number :
        print(f"You got it! The answer was {number}")
        break
      elif player_guess < number < player_guess + 5 :
        print("Low. Close!")
      elif player_guess > number > player_guess - 5 :
        print("High. Close!")
      elif player_guess < number :
        print("Too Low.")  
      elif player_guess > number :
        print("Too High.")
      
      remaining_attempts -= 1
      if remaining_attempts > 0:
        print("        Guess agian.")
    
    guessNumber()
guessNumber()