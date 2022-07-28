print("This calculator solves an equation of the form ax + b = c.")

a = float(input("Please input value for 'a'. "))
b = float(input("Please input value for 'b'. "))
c = float(input("Please input value for 'c'. "))

def linearSolve(a, b, c):
  if a != 0 and b!= 0 and c!= 0 and a != '' and b != '' and c != '':
    d = c - b
    x = d / a
    return x
  else: 
    print("Your parameters are invalid.")

print("The value of x is " + str(linearSolve(a, b, c)) + ".")

  