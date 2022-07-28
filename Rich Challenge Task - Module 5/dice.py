

faces = input("How many faces does each dice have? ")
dice = input("How many dice are you using? ")
trials = input("How many trials are you performing? ")
import random
def simulateDice(faces, dice):
  sum = 0
  for el in range(int(dice)):
    sum += random.randint(1, int(faces))
  return sum

data = []
for el in range(1, (int(dice) * int(faces) + 1)):
  data.append(0)
  
def generateData(faces, dice, trials, data):
  for x in range(int(trials)):
    plus = simulateDice(faces, dice)
    data[plus - 1] += 1
  return data 

datax = list(range(1, (int(dice) * int(faces) + 1)))
datay = generateData(faces, dice, trials, data)
title = "Dice Outcomes"
horlabel = "Outcomes"
verlabel = "Frequencies"

print(datax)
print(datay)

# Could not import matplotlib.
# def createGraph(datax, datay, title, horlabel, verlabel):
  # plt.bar(datax, datay)
  # plt.xlabel(horlabel)
  # plt.ylabel(verlabel)
  # plt.title(title)
  # plt.show

# createGraph(datax, datay, title, horlabel, verlabel)



  
  
  
    
  






  