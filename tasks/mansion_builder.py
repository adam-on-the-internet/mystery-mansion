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

def get_rooms():
  rooms = read_rooms()
  random.shuffle(rooms)
  return rooms

def get_locked_spaces(spaces):
  lockable_spaces = []
  for space in spaces:
    if space.can_be_locked:
      lockable_spaces.append(space.name)
  random.shuffle(lockable_spaces)
  return lockable_spaces[:2]  

def populate_spaces():
  rooms = get_rooms()
  spaces = read_spaces()
  locked_spaces = get_locked_spaces(spaces)

  for index, space in enumerate(spaces):
    space.is_locked = space.name in locked_spaces
    space.room_name = rooms[index].name
  return spaces

def setup_spaces(id):
  spaces = populate_spaces()
  lines = []
  for space in spaces:
    locked_message = " [LOCKED]" if space.is_locked else ""
    lines.append("- (" + space.game_code + ") " + space.room_name + locked_message)

  add_line_to_file("## Rooms", id)
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
  setup_spaces(id)
  setup_furniture(id)
  setup_interactions(id)
  # TODO each space needs:
  #   furniture
  # TODO each furniture needs
  #   interaction
  # TODO each HINT interaction needs
  #   requirement
  #   type
  #   message
