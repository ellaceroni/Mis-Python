string = "Caterpillar"
def vowelRemove(string):
  word = ""
  for x in string:
    if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" and x != "y":
      word += x
  new_word = word[len(word) - 1: : -1]
  print(new_word)

vowelRemove(string)