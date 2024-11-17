#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# # Steps of completion :
# # 1. Create a for-loop where for each letters chosen the program randomly chooses char from letters[] until all letters have been choosen.
# new_password_letter = random.sample(letters, nr_letters)
# # 2. Create a for-loop where for each symbols chosen, the program randomly chooses symbols from symbols[] until all symbols have been choosen.
# new_password_symbol = random.sample(symbols, nr_symbols)
# # 3. Create a for-loop where for each numbers chosen, the program randomly chooses number from numbers[] until all number have been choosen.
# new_password_number = random.sample(numbers, nr_numbers)
# # 4. Add all of them togather and print them.
# new_password_list = new_password_letter + new_password_symbol + new_password_number
# new_password = ''.join(new_password_list)
# print(f"Your new password should be: {new_password}\nOr,")
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# options = [letters, numbers, symbols]
# count = [nr_letters, nr_numbers, nr_symbols]
# password = []

# for t in range(0, sum(count)):
#   while True:
#     chosen_random_list = random.randint(0, len(count) - 1)
#     if count[chosen_random_list] > 0:
#       break

#   chosen_password_char = random.choice(options[chosen_random_list])
#   password.append(chosen_password_char)
#   count[chosen_random_list] -= 1

# # print(password)
# final_password = ''.join(password)
# print(f"Your new password should be: {final_password}")\


# Instructor's way
# Easy level

# password1 = ""

# for char in range(1, nr_letters + 1):
#   password1 += random.choice(letters)
#   # print(password1)

# for char in range(1, nr_symbols + 1):
#   password1 += random.choice(symbols)
#   # print(password1)

# for char in range(1, nr_numbers + 1):
#   password1 += random.choice(letters)
#   # print(password1)

# print(password1)

# Hard Level

password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)
  # print(password1)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
  # print(password1)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(letters)
  # print(password1)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password2 = ""
for char in password_list:
  password2 += char

print(f"Your password is: {password2}")