def isValid(code):
  new_code = ""
  for el in code:
    if el != " ":
      new_code += el
  return len(new_code) == 6 and new_code[0].isalpha() and new_code[2].isalpha() and new_code[4].isalpha() and new_code[1].isdigit() and new_code[3].isdigit() and new_code[5].isdigit()
    

  
      
