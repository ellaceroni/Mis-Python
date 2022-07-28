list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
def is_identity(list):
  index = 0
  cont = True 
  for el in list:
    sum = 0
    if cont:
      for x in el:
        sum += x
        if el[index] == 1 and sum == 1:
          cont = True
        else:
          cont = False
    index += 1
  print(cont) 

is_identity(list)