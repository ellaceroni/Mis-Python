teams = int(input("How many teams are playing? Answer must be even and between 4 and 20. "))
import random

def randomNum(listing):
  index = random.randint(0, len(listing) - 1)
  return listing.pop(index)

def schedule(teams):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  teamList = []
  for el in range(teams):
    teamList.append(alphabet[el])
  print(teamList)
  
  teamPairs = []
  while teamList:
    rand1 = randomNum(teamList)
    rand2 = randomNum(teamList)
    pair = rand1, rand2
    teamPairs.append(pair)
  for x in range(len(teamPairs)):
    print("Pair " + str(x + 1) + ": " + str(teamPairs[x]))

schedule(teams)