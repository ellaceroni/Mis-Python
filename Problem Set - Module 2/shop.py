def information():
  location = input("Do you live in Ontario? Answer 'y' or 'n'. ")
  if location == 'y' or location == 'Y':
    taxRate = 0.13
  else:
    taxRate = float(input("Input your tax rate as a decimal. "))

  price = float(input("What is the total cost of your goods? "))
  
  age = float(input("Enter your age. "))
  member = input("Are you a member of the store? Answer 'y' or 'n'. ")
  if age < 18 or age >= 65 and member == 'y' or member == 'Y':
    discount = 0.85
  else:
    discount = 1

  return (price * discount) + (price * discount * taxRate)

print(information())
  
    