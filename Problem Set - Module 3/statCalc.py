def min(first, second):
  if first <= second:
    return first
  else:
    return second

def max(first, second):
  if first >= second:
    return first
  else:
    return second

def average(total, items):
  return format(total / items, '.2f')

def stats():
  min_ = 0
  max_ = 0
  average_ = 0
  counter = 0
  sum = 0
  userInput = input("What number would you like to input? Press 'q' to quit. ")
  while userInput != 'q' and userInput != "Q":
    sum += int(userInput)
    counter += 1
    max_ = max(max_, int(userInput))
    min_ = min(min_, int(userInput))
    userInput = input("What number would you like to input? Press 'q' to quit. ")
  print(max_)
  print(min_)
  print(average(sum, counter))

print(stats())
    
    