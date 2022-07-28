import random 

def listGen(n, N):
  list = []
  for x in range(0, 11):
    new = random.randint(int(n), int(N))
    list.append(new)
  return(list)
  

def torque(list):
  index = 0
  sum = 0
  for x in list:
    length = index / 10
    distance = 0.5 - length
    weight = distance * x
    sum += weight
    index += 1
  if sum > 0:
    return "counterclockwise"
  elif sum == 0:
    return "does not move!"
  else:
    return "clockwise"

print("Welcome to the torque game!")
play = input("Would you like to play? (y/n) ")
while play == "y":
  N = input("What is the max weight you would like to play with? ")
  n = input("What is the min weight you would like to play with? ")
  print("Here is the generated ruler and weights.") 
  list = listGen(n, N)
  print(list)
  print("                 ^                ")

  answer = input("Will this system tilt clockwise (a), counterclockwise (b), or remain stable (c)?")

  if answer == "a" and torque(list) == "clockwise" or answer == "b" and torque(list) == "counterclockwise" or answer == "c" and torque(list) == "does not move!":
    print("You guessed it!")
  else:
    print("Incorrect! The correct answer was " + str(torque(list)) + ".")
  play = input("Would you like to play again? (y/n) ")
else:
  print("Goodbye!")

