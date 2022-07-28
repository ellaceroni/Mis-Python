salaries = [50, 80, 90, 50, 75, 20, 99, 88, 33, 60]
percentages = [50, 0, 0, 10, 10, 20, 0, 0, 0, 10]

def salaryUpdate(salaries, percentages):
  new_salaries = []
  for index in range(len(salaries)):
    decimal = 1 + percentages[index] / 100
    new_salaries.append(format(decimal * salaries[index], '.2f'))
  print(new_salaries)

salaryUpdate(salaries, percentages)