import math

def computeValue(n, r):
  value = math.factorial(n) / (math.factorial(n - r) * math.factorial(r)) 
  return value 

rows = int(input("How many rows would you like to compute? "))
list = []
def generateTriangle(rows):
  index = 1
  while index <= rows:
    list.append([0 for y in range(index)])
    index += 1
  return list

list = generateTriangle(rows)

def generatePascal(list):
  index = 0
  for n in range(len(list)):
    for r in range(len(list[index])):
      list[n][r] += computeValue(n, r)
    index += 1
  return list

result = generatePascal(list)

for el in result:
  print(el)
    
  