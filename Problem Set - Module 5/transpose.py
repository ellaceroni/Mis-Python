
matrix = [[2, 3, 4], [1, 5, 8]]

result = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]

def tranpose(matrix, result):
  for x in range(len(matrix)):
    for y in range(len(matrix[0])):
      result[y][x] = matrix[x][y]
  print(result)

tranpose(matrix, result)


    
  