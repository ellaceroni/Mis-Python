import random 
def isSet(list):
  new_list = []
  for el in list:
    if el not in new_list:
      new_list.append(el)
  if len(new_list) != len(list):
    print(False)
  else:
    print(True)

number = input("How many items in the list? ")
low = input("What is the lower bound? ")
high = input("What is the upper bound? ")
def randomSet(number, low, high):
  lst = []
  for x in range(int(number)):
    lst.append(random.randint(int(low), int(high) + 1))
  return lst
    
result = randomSet(number, low, high)

print(result)

isSet(result)