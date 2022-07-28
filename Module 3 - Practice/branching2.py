def guessTheNumber():
  answer = input("Is the number greater than or equal to five? ")
  if answer == "y":
    answer = input("Is the number greater than or equal to 7? ")
    if answer == "y":
      answer = input("Is the number 7? ")
      if answer == "y":
        return "I guessed it!"
      else:
        return "Your number must be 8."
    else:
      answer = input("Is the number 5? ")
      if answer == "y":
        return "I guessed it!"
      else:
        return "Your number must be 6."
  else:
    answer = input("Is the number greater than or equal to 3?")
    if answer == "y":
      answer = input("Is the number 3?")
      if answer == "y":
        return "I guessed it!"
      else:
        return "Your number must be 4."
    else:
      answer = input("Is the number 1? ")
      if answer == "y":
        return "I guessed it!"
      else:
        return "Your number must be 2."

print(guessTheNumber())
    
  