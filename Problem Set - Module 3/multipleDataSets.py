cutoffFrequency = float(input("What is the cutoff frequency? "))
wordFileName = input("What is the word file name? ")
freqFileName = input("What is the frequency file name? ")
def reading(wordFileName, freqFileName, cutoffFrequency):
  fileObject1 = open(wordFileName, "r")
  fileObject2 = open(freqFileName, "r")
  next_line1 = fileObject1.readline()
  next_line2 = fileObject2.readline()
  counter = 0
  while next_line1 != 0 and next_line2 != 0:
    if float(next_line2) >= cutoffFrequency:
      print(str(next_line1) + " has a frequency of " + str(next_line2))
      counter += 1
    next_line1 = fileObject1.readline()
    next_line2 = fileObject2.readline()
  print("There are " + str(counter) + " words with a frequency greater than " + str(cutoffFrequency) + ".")

print(reading(wordFileName, freqFileName, cutoffFrequency))