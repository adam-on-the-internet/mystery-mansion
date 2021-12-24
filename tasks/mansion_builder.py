from tasks.game_file_writer import add_line_to_file, add_lines_to_file
from tasks.info_reader import read_furniture, read_rooms, read_spaces, read_interactions
import random

def populate_interactions():
  # prep interactions
  interactions = get_interactions()
  random.shuffle(interactions)
  # prep furniture
  furniture = read_furniture()
  random.shuffle(furniture)
  # prep add interactions to furniture
  for index, interaction in enumerate(interactions):
    interaction.furniture_name = furniture[index].name
  return interactions  

def setup_interactions(id):
  interactions = populate_interactions()
  lines = []
  for interaction in interactions:
    lines.append("- " + interaction.furniture_name + " : " + interaction.name)
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

def get_interactions():
  interactions = read_interactions()
  random.shuffle(interactions)
  return interactions

def setup_mansion(id):
  print("setting up mansion...")
  setup_spaces(id)
  setup_interactions(id)
  # TODO each room needs:
  #   furniture
  # TODO each HINT interaction needs
  #   requirement
  #   type
  #   message
