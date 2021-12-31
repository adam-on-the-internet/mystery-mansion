from util.file_utils import make_directory_if_not_exists
import datetime

def add_lines_to_file(lines, id):
  mansion_file = get_mansion_file_path(id)
  f = open(mansion_file, "a")
  for line in lines:
    f.write(line)
    f.write("\n")
  f.close()

def setup_mansion_file(id):
  mansion_file = get_mansion_file_path(id)
  f = open(mansion_file, "w")
  f.close()  

def get_mansions_directory():
  return "_mansions/"

def get_mansion_directory(id):
  mansion_directory = get_mansions_directory()
  return mansion_directory + id + "/"

def get_mansion_file_path(id):
  mansion_directory = get_mansion_directory(id)
  return mansion_directory + "mansion.md"

def setup_mansions_directory():
  mansions_directory = get_mansions_directory()
  make_directory_if_not_exists(mansions_directory)

def setup_mansion_directory(id):
  game_directory = get_mansion_directory(id)
  make_directory_if_not_exists(game_directory)

def setup_directories(id):
  setup_mansions_directory()
  setup_mansion_directory(id)

def setup_save_file(id):
  setup_directories(id)
  setup_mansion_file(id)

def write_mansion_title(mansion):
  now = datetime.datetime.now()
  lines = [
    "# Mystery Mansion",
    "",
    "- style: " + mansion.style,
    "- id: " + mansion.id,
    "- generated: " + str(now),
    ""
  ]
  add_lines_to_file(lines, mansion.id) 

def write_mansion_clues(mansion):
  lines = [
    "## Clues",
    "",
  ]
  for asset in mansion.assets:
    line = "- " + asset.to_string()
    lines.append(line)
  lines.append("")
  add_lines_to_file(lines, mansion.id) 

def write_mansion_rooms(mansion):
  lines = [
    "## Rooms",
    "",
  ]
  for space in mansion.spaces:
    lines.append("### " + space.to_string())
    lines.append("")
    lines.append("Furniture: (" + str(len(space.interactions)) + " items)")
    lines.append("")
    for interaction in space.interactions:
      lines.append("- " + interaction.to_string())
    lines.append("")
  lines.append("")
  add_lines_to_file(lines, mansion.id) 

def write_mansion_details(mansion):
  write_mansion_title(mansion)
  write_mansion_clues(mansion)
  write_mansion_rooms(mansion)

def save_mansion(mansion):
  setup_save_file(mansion.id)
  write_mansion_details(mansion)
