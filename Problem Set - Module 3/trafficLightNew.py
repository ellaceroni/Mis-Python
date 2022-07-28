def light(colour):
  if colour == "b" or colour == "B":
    print("Green")
  elif colour == "g" or colour == "G":
    print("Yellow")
  elif colour == "y" or colour == "Y":
    print("Red")
  elif colour == "r" or colour == "R":
    print("Blue")
  else:
    print("Invalid colour.")

def result():
  user = input("What colour is the light? ")
  while user != "q" and user != "Q":
    light(user)
    user = input("What colour is the light? ")
  print("Goodbye!")
  

result()
  