name = "ella ceroni"
def upper(name):
  index = 0
  letter = name[index]
  while letter != " ":
    index += 1 
    letter = name[index]
  name = name[index + 1:]
  name = name[0].upper() + name[1:]
  print(name)
    
upper(name)
    