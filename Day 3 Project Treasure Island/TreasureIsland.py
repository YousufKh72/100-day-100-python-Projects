print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Upon entering the island you see two roads.")
first_choice = input("Which way will you go? Left or Right? - ").lower()

if first_choice != "left":
  print("You fell into a dark hole, alone to die!\nGAME OVER.")
else:
  print("Now you stumbled upon a river. You can swim or wait for a boat.")
  second_choice = input("What will you do? Swim or Wait? ").lower()
  if second_choice != "wait":
    print("The river had vicious piranha who devoured you!\nGAME OVER.")
  else:
    print("You waited! Smart move. A boat came and now you are on the other side.")
    print("Now you have arrived at a cave with 3 colored doors. which one will you choose?")
    door_choice = input("Red, Blue or Yellow? ").lower()
    if door_choice == "red":
      print("Oh no! You have fallen into a pit of fire!\nGAME OVER.")
    elif door_choice == "blue":
      print("Waiting there was hungry beasts. You got eaten.\nGAME OVER.")
    elif door_choice == "yellow":
      print ("Smart move the whole way! You are a true treasure hunter.")
      print ("You have reached at the end of the island and recieved the greatest treasure of all. Your life!")
      print ("Enjoy your treasure.\YOU WIN!")
    else:
      print("You thought there was another way? You wish!")
      print("Other hunters found you and skinned you.")
      print("GAME OVER.")