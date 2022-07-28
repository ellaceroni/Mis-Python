list = [1, 2, 3, 4]
shiftNum = -2
def shift(list, shiftNum):
  print(list[-shiftNum:] + list[:-shiftNum])
  
shift(list, shiftNum)   
    