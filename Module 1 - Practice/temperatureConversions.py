userInput = input("What is the temperature in degrees Celsius? ")
tempC_float = float(userInput)
tempF_float = 9/5 * tempC_float + 32
tempF_string = str(tempF_float)
print(userInput + "C = " + tempF_string + "F")

# Rounded answer.
tempF_float = round(tempF_float, 2)
tempF_string = str(tempF_float)
print(userInput + "C = " + tempF_string + "F")