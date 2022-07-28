list = [1, 2, 3, 4, 5]
def copy(list):
  index = -1
  new_list = []
  while index + 1 < len(list):
    index += 1
    new_list.append(list[index])
  new_list.append('This value will be only in copied list.')
  print(new_list)
  print

copy(list)