email = "ellaceroni@gmail.com"
def emailMask(email):
  new_email = ""
  index = email.find("@")
  for x in email[0:index]:
      if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" and x != "y":
        new_email += x
      else:
        new_email += "*"
  new_email += "@"
  for x in email[index + 1:]:
      if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" and x != "y":
        new_email += x
      else:
        new_email += "#"
  print(new_email)

emailMask(email)
  
  