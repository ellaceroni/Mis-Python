term = input("What is the term number? Make sure it is a triangle number! ")
symbol = input("What symbol would you like to use? ")

def triangle(term, symbol):
  space = " "
  jump = symbol + space
  num = int((- 1 + (1 - (4 * (- 2 * int(term)))) ** 0.5) / 2)
  space_start = num - 1
  lst = []
  for x in range(num):
    lst.append(str(space_start * space) + str(jump * (x + 1)))
    space_start -= 1
  for el in lst:
    print(el)
  
triangle(term, symbol)
    

   

