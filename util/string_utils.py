import string
import random

def get_four_letter_id():
  id = ""
  letters = string.ascii_letters
  while len(id) != 4:
    letter = random.choice(letters)
    id = id + letter.upper()
  return id  