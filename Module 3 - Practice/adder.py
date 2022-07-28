number = int(input("What is the number? "))
def add(number):
  value = 0
  counter = 1
  while counter <= number:
    value += counter
    counter += 1
  return "The adder value is " + str(value) + "."
print(add(number))