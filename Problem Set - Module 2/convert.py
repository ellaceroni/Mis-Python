temperature = input("What is the temperature? ")

unit = input("What is the unit of temperature? Use 'c' and 'f' for Celsius and Farenheit, respectively. ")

def celsiusToF(temperature):
  newTempF = float(temperature) * 5/8 + 32
  return format(newTempF, '.2f')

def farenheitToC(temperature):
  newTempC = (float(temperature) - 32) * 8/5
  return format(newTempC, '.2f')

if unit == 'c':
  print("The temperature is " + str(celsiusToF(temperature)) + " degrees Farenheit.")
if unit == 'f':
  print("The temperature is " + str(farenheitToC(temperature)) + " degrees Celsius.")