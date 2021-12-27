from tasks.game_file_writer import add_lines_to_file, setup_directories, setup_game_file
from util.file_utils import make_directory_if_not_exists
import uuid
import datetime

def get_id():
  return str(uuid.uuid4())

def get_name():
  return "Find the Money" # TODO randomize game name

def describe_game(id, name):
  now = datetime.datetime.now()
  lines = [
    "# Mystery Mansion: " + name,
    "- id: " + id,
    "- generated: " + str(now),
  ]
  add_lines_to_file(lines, id)  

def initialize_game():
  id = get_id()
  name = get_name()
  setup_directories(id)
  setup_game_file(id)
  describe_game(id, name)
  return id
