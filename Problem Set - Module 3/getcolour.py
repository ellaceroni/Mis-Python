wavelength = float(input("What is the wavelength in nanometres? "))
def getcolour(wavelength):
  if wavelength >= 380 and wavelength <= 450:
    return "violet."
  elif wavelength > 450 and wavelength <= 495:
    return "blue."
  elif wavelength > 495 and wavelength <= 570:
    return "green."
  elif wavelength > 570 and wavelength <= 590:
    return "yellow."
  elif wavelength > 590 and wavelength <= 620:
    return "orange."
  elif wavelength > 620 and wavelength <= 750:
    return "red."
  else:
    return "unknown."

print("The light is " + str(getcolour(wavelength)))