list = [1, 2, 3, 4, 5]

def swap(list):
  new_list = []
  if len(list) % 2 != 0:
    middle_index = len(list) // 2
    middle = list[middle_index]
    first = list[0:middle_index]
    last = list[middle_index + 1:len(list) + 1]
    new_list.extend(last)
    new_list.append(middle)
    new_list.extend(first)
  else:
    first = list[0:len(list) / 2]
    last = list[len(list) / 2:len(list) + 1]
    new_list.extend(last)
    new_list.extend(first)
  print(new_list)

swap(list)