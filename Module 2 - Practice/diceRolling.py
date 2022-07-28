import random
outcome = random.randint(2, 12)
def decide(choice, outcome):
  
  if outcome > 7 and choice == "h":
    return 1
  if outcome < 7 and choice == "l":
    return 1
  if outcome == 7:
    return 0
  else:
    return -1 

choice = input("Choose high (h) or low (l) roll. ")

print("The dice outcome was " + str(outcome) + ".")

decision = decide(choice, outcome)

def winLoss(decision):
  if decision == 1:
    print("You Win!")
  if decision == -1:
    print("You Lose!")
  else:
    print("Tie!")

print(winLoss(decision))

