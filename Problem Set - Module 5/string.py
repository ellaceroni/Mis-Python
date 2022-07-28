string = "I like cats and dogs."
def toList(string):
  new_list = []
  for el in string:
    new_list.append(el)
  print(new_list)
  
def toString(list):
  new_string = ""
  for x in list:
    new_string += x
  print(new_string)

def replace(strng, replaced, replacement):
  new_string2 = ""
  for el in strng:
    if el != replaced:
      new_string2 += el
    else:
      new_string2 += replacement
  print(new_string2)

strng = "I like cats and dogs."
replaced = "a"
replacement = "@"

replace(strng, replaced, replacement)