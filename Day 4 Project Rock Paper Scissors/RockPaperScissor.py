rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
# def choice(n):
#   if n == 0:
#     return(rock)
#   elif n == 1:
#     return(paper)
#   elif n == 2:
#     return(scissors)
game_images = [rock, paper, scissors]
# Ask the user for their choice. 0 for Rock, 1 for Paper or 2 for Scissors.
user = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
while user < 0 or user >= 3:
  user = int(input("You typed an invalid number, try again!\n"))
print(f"\nYou Chose {game_images[user]}")
# Let the computer randomly choose between (0,2) for its own choice
pc = random.randint(0,2)
print(f"Computer Chose {game_images[pc]}")
# Decide who wins the game by creating multiple scenario.

def game(user, pc):
  if user == 0 and pc == 1:
    return("You Lose.")
  elif user == 1 and pc == 2:
    return("You Lose.")
  elif user == 2 and pc == 0:
    return("You Lose.")
  elif user == 0 and pc == 2:
    return("You Win.")
  elif user == 1 and pc == 0:
    return("You Win.")
  elif user == 2 and pc == 1:
    return("You Win.")
  else :
    return("Its a tie!")

# Or this can be done as below
# if user == 0 and pc == 2:
#   print("You Win!")
# elif pc == 0 and user == 2:
#   print("You Lose!")
# elif pc > user:
#   print("You Lose!")
# elif user > pc:
#   print("You Win!")
# else :
#   print("Its's a draw")

# Print the decision
print(game(user,pc))