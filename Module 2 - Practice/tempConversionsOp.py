def tempConvert(degCelsius):
  degFar = 9 / 5 * degCelsius + 32
  return degFar

celsius = float(input("What is the temperature in degrees Celsius? "))

print("The temperature is " + str(tempConvert(celsius)) + " degrees farenheit.")