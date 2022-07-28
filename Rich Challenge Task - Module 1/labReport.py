fileObject = open("measurements.txt", "r")

# Store each measurement in a variable.
first = fileObject.readline()
second = fileObject.readline()
third = fileObject.readline()
fourth = fileObject.readline()
fifth = fileObject.readline()
expected = fileObject.readline()

# Calculate average.
average = (float(first) + float(second) + float(third) + float(fourth) + float(fifth)) / 5

# Calculate standard deviation.
summation = (float(first) - average) ** 2 + (float(second) - average) ** 2 + (float(third) - average) ** 2 + (float(fourth) - average) ** 2 + (float(fifth) - average) ** 2

standardDeviation = (summation / 5) ** 0.5

# Calculate t-score.

tScore = abs(average - float(expected)) / standardDeviation

# Write on conclusions.txt.

fileObject2 = open("conclusions.txt", "r+")
fileObject2.write("Lab Results: " + "\nAverage = " + str(round(average, 2)) + "\nStandard Deviation = " + str(round(standardDeviation, 2)) + "\nT-Score = " + str(round(tScore, 2)))
fileText = fileObject2.read(-1)

print(fileText + "\nhas been successfully saved in the conclusions.txt file.")

fileObject.close()
fileObject2.close()


          
          
  