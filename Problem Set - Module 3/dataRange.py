fileName = input("Please input file name. ")
lowBoundary = float(input("Please input low boundary. "))
highBoundary = float(input("Please input high boundary. "))

def check(fileName, lowBoundary, highBoundary):
  if lowBoundary > highBoundary:
    print("Error.")
  else:
    fileObject = open(fileName, "r")
    next_line = fileObject.readline()
    counter = 0
    sum = 0
    while next_line != "":
      if float(next_line) >= lowBoundary and float(next_line) <= highBoundary:
        print("Data point " + next_line + " has been added.")
        counter += 1
        sum += float(next_line)
      next_line = fileObject.readline()
  print("The average of the values is " + str(format(sum / counter, '.2f')) + ".")

print(check(fileName, lowBoundary, highBoundary))