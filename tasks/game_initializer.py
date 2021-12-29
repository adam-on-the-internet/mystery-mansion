from util.file_utils import make_directory_if_not_exists
import datetime
import random
import string

def get_id():
  id = ""
  while len(id) != 4:
    next_letter = random.choice(string.ascii_letters).upper()
    id = id + next_letter
  return id

def initialize_game():
  id = get_id()
  return id
