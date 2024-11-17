import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# HINT: Use clear() to clear the console output.

from art import logo

def if_integer(n):
  if float(n).is_integer():
    return int(n)
  return n

#Calculator

#Add
def add(n1, n2):
  """Returns the sum of n1 and n2."""
  return n1 + n2

#Subtract
def subtract(n1, n2):
  """Returns the difference between n1 and n2."""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """Returns the product of n1 and n2."""
  return n1 * n2

#Divide
def divide(n1, n2):
  """Returns the quotient of n1 by n2."""
  if n2 == 0:
    return "Can not divide by zero."
  return n1 / n2

#Exponent
def exponent(n1, n2):
  """Returns the square of n1 by n2."""
  if n2 == 0:
    return 1
  elif n1 == 0:
    return 0
  return n1 ** n2

operations = { "+"  : add,
               "-"  : subtract,
               "*"  : multiply,
               "/"  : divide,
               "^" : exponent,
             }
def calculator():
  clear()
  print(logo)
  num_1 = float(input("What's the first number?: "))
  num_1 = if_integer(num_1)
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue == True:
    operator = input("Pick an operation: ")
    num_2 = float(input("What's the next number?: "))
    num_2 = if_integer(num_2)
    calculator_function = operations[operator]
    result = calculator_function(num_1, num_2)
    result = if_integer(result)
    print(f"{num_1} {operator} {num_2} = {result}")
    to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
    if to_continue == "y":
      num_1 = result
    else :
      should_continue = False
      calculator()

calculator()