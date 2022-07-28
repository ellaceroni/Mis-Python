print("This calculator solves a linear-quadratic system of the form:\n y = ax^2 + bx + c\n y = mx + d ")

a = float(input("Please input an 'a' value. "))
b = float(input("Please input a 'b' value. "))
c = float(input("Please input a 'c' value. "))
m = float(input("Please input an 'm' value. "))
d = float(input("Please input a 'd' value. "))

def solve(a, b, c, m, d):
  if a != 0 and a != '' and b != '' and c != '' and m != '' and d != '':
    e = b - m
    f = c - d
    if e * e > 4 * a * f:
      x1 = (- e + ((e * e - (4 * a * f)) ** 0.5)) / (2 * a)
      x2 = (-e - ((e * e - (4 * a * f)) ** 0.5)) / (2 * a)
      y1 = m * x1 + d
      y2 = m * x2 + d
      print("The solutions are (" + str(x1) + ", " + str(y1) + ") " + "and (" + str(x2) + ", " + str(y2) + ").")
    else:
      print("Unsolvable system of equations.")
  else:
    print("Invalid entries.")

print(solve(a, b, c, m, d))