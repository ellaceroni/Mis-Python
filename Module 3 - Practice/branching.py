percentage = float(input("What is the mark in percentage form? "))
def marks(percentage):
  if percentage >= 80:
    return "Level 4"
  elif percentage >= 70 and percentage <= 79:
    return "Level 3"
  elif percentage >= 60 and percentage <= 69:
    return "Level 2"
  elif percentage >= 50 and percentage <= 59:
    return "Level 1"
  else:
    return "Level R"

print(marks(percentage))
  