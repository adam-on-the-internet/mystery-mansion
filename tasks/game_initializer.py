from tasks.game_file_writer import add_lines_to_file, setup_directories, setup_game_file
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

def describe_game(id):
  now = datetime.datetime.now()
  lines = [
    "# Mystery Mansion",
    "- id: " + id,
    "- generated: " + str(now),
  ]
  add_lines_to_file(lines, id)  

def initialize_game():
  id = get_id()
  setup_directories(id)
  setup_game_file(id)
  describe_game(id)
  return id
