from util.file_utils import make_directory_if_not_exists

def add_line_to_file(line, id):
  add_lines_to_file([line], id)

def add_lines_to_file(lines, id):
  setup_file = get_setup_file_path(id)
  f = open(setup_file, "a")
  
  for line in lines:
    f.write(line)
    f.write("\n\n")

  f.close()

def open_blank_setup_file(id):
  setup_file = get_setup_file_path(id)
  f = open(setup_file, "w")
  f.close()  

def get_games_directory():
  return "games/"

def get_game_directory(id):
  games_directory = get_games_directory()
  return games_directory + id + "/"

def get_setup_file_path(id):
  game_directory = get_game_directory(id)
  return game_directory + "setup.md"

def initialize_game_file():
  print("initialize game file...")

  # setup game variables
  id = "asdf1234" # TODO randomize
  name = "The First Game" # TODO randomize

  # verify game directory is setup
  games_directory = get_games_directory()
  make_directory_if_not_exists(games_directory)

  # create game directory
  game_directory = get_game_directory(id)
  make_directory_if_not_exists(game_directory)

  # initialize the game file
  open_blank_setup_file(id)
  lines = [
    "# Mystery Mansion: " + name,
    "GAME ID: " + id,
  ]
  add_lines_to_file(lines, id)

  return id
