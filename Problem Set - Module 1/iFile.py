fileName = input("What would you like to name the file? ")
fileContent = input("Enter a single line of text to be saved to the file: ")
fileName += ".txt"
fileObject = open(fileName, "w")
fileObject.write(fileContent)
fileObject.close()
print("The content " + "\"" + fileContent + "\",\n" + "has been successfully saved in the file " + fileName + "!")