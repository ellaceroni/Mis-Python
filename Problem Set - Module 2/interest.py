interestRate = input("What is the interest rate? ")
principal = input("What is the principal? ")

def simpleInt(interestRate, principal):
  simpleInterest = (float(interestRate) / 100) * float(principal)
  return format(simpleInterest, '.2f')

print("Your simple interest amount is $" + simpleInt(interestRate, principal))