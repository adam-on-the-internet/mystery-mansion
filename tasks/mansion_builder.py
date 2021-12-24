from tasks.game_file_writer import add_line_to_file, add_lines_to_file
from tasks.info_reader import read_furniture, read_rooms, read_spaces, read_interactions
import random

def setup_furniture(id):
  furniture = read_furniture()
  random.shuffle(furniture)
  
  lines = []

  for furn in furniture:
    lines.append("- " + furn.name + " (" + furn.game_code + ")")

  add_line_to_file("## Furniture", id)
  add_lines_to_file(lines, id)

def setup_rooms(id):
  rooms = read_rooms()
  random.shuffle(rooms)
  
  lines = []

  for room in rooms:
    lines.append("- " + room.name)

  add_line_to_file("## Rooms", id)
  add_lines_to_file(lines, id)

def setup_spaces(id):
  spaces = read_spaces()
  
  lines = []

  for space in spaces:
    lines.append("- " + space.name)

  add_line_to_file("## Spaces", id)
  add_lines_to_file(lines, id)

def setup_interactions(id):
  interactions = read_interactions()
  random.shuffle(interactions)
  lines = []
  for interaction in interactions:
    lines.append("- " + interaction.name)
  add_line_to_file("## Interactions", id)
  add_lines_to_file(lines, id)    

def setup_mansion(id):
  print("setting up mansion...")
  setup_furniture(id)
  setup_rooms(id)
  setup_spaces(id)
  setup_interactions(id)
  # TODO each space needs:
  #   locked or unlocked
  #   room name
  #   furniture
  # TODO each furniture needs
  #   interaction
  return
