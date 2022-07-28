import math
mass = input("What is the mass of the object? ")
magFile = input("What is the name of the file holding the magnitudes? ")
dirFile = input("What is the name of the file holding the directions? ")

def newton(mass, magFile, dirFile):
  fileObject1 = open(magFile)
  fileObject2 = open(dirFile)
  next_line1 = fileObject1.readline()
  next_line2 = fileObject2.readline()
  xSum = 0
  ySum = 0
  while next_line1 != "" and next_line2 != "":
    print("The x-component and y-component of " + str(next_line1) + " at " + str(next_line2) + " radians to the x-axis are " + str(float(next_line1) * math.cos(float(next_line2))) + " and " + str(float(next_line1) * math.sin(float(next_line2))) + " respectively.")
    xSum += float(next_line1) * math.cos(float(next_line2))
    ySum += float(next_line1) * math.sin(float(next_line2))
    next_line1 = fileObject1.readline()
    next_line2 = fileObject2.readline()
  print("The net force is " + str((xSum ** 2 + ySum ** 2) ** 0.5) + " Newtons at " + str(math.atan(ySum / xSum)) + " radians relative to the x-axis. The acceleration is thus " + str(((xSum ** 2 + ySum ** 2) ** 0.5) / float(mass)) + " metres per second squared in the same direction.")
      
newton(mass, magFile, dirFile)

