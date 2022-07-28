point = 6
dataSet = [1, 2, 3, 4, 5]

def isIn(dataSet, point):
  index = -1
  checkPoint = dataSet[index]
  empty_list = []
  while checkPoint != point and index + 1 < len(dataSet):
    index += 1
    checkPoint = dataSet[index]
    empty_list.append(checkPoint)
  if len(empty_list) != len(dataSet):
    print(str(point) + " is in the list.")
  else:
    print(str(point) + " is not in the list.")
    
isIn(dataSet, point)
