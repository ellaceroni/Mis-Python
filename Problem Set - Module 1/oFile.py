fileName = input("What is the name of the file? ")
fileObject = open(fileName, "r")
fileText = fileObject.read()
print("The content, " + "\"" + fileText + "\" " + "has been successfully retrieved from the file " + fileName)