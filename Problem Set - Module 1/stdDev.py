firstMeasurement = input("What is the first measurement? ")
secondMeasurement = input("What is the second measurement? ")
thirdMeasurement = input("What is the third measurement? ")

# Calculate average.
average = (float(firstMeasurement) + float(secondMeasurement) + float(thirdMeasurement)) / 3

# Calculate summation.
summation = (float(firstMeasurement) - average) ** 2 + (float(secondMeasurement) - average) ** 2 + (float(thirdMeasurement) - average) ** 2

standardDeviation = (summation / 3) ** 0.5

print("The standard deviation for the measurements " + "(" + firstMeasurement + ", " + secondMeasurement + ", " + thirdMeasurement + ") " + "is " + str(round(standardDeviation, 2)))