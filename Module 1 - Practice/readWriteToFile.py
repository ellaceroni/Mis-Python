fileObject = open("test.txt", "r")
fileText = fileObject.read()
fileName = fileObject.name
print("The file, " + fileName + "has the following content\n" + fileText)
fileObject.close()