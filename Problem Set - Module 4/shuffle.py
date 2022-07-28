list1 = [1, 3, 5]
list2 = [2, 4, 6]
def shuffle(list1, list2):
  index = -1
  new_list = []
  while index + 1 < len(list1) and index + 1 < len(list2):
    index += 1
    new_list.append(list1[index])
    new_list.append(list2[index])
  print(new_list)

shuffle(list1, list2)
    