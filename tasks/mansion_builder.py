from tasks.game_file_writer import add_line_to_file, add_lines_to_file
from tasks.info_reader import read_furniture, read_rooms, read_spaces, read_interactions
import random

def populate_interactions():
  interactions = read_interactions()
  random.shuffle(interactions)
  furniture = read_furniture()
  for index, interaction in enumerate(interactions):
    interaction.furniture = furniture[index]
  return interactions  

def setup_interactions(id):
  interactions = populate_interactions()
  lines = []
  for interaction in interactions:
    lines.append("- " + interaction.furniture.name + " : " + interaction.name + " : " + interaction.furniture.selected_room)
  add_line_to_file("## Furniture", id)
  add_lines_to_file(lines, id)
  return interactions

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

def populate_spaces(interactions):
  rooms = get_rooms()
  spaces = read_spaces()
  locked_spaces = get_locked_spaces(spaces)

  for index, space in enumerate(spaces):
    space.is_locked = space.name in locked_spaces
    space.room = rooms[index]
    space.interactions = []
    for interaction in interactions:
      if space.room.name in interaction.furniture.rooms:
        # TODO handle if multiple rooms are available...
        space.interactions.append(interaction)
  return spaces

def setup_spaces(id):
  interactions = setup_interactions(id)
  # TODO one clue in each room MAX

  spaces = populate_spaces(interactions)
  lines = ["## Rooms"]
  for space in spaces:
    locked_message = " [LOCKED]" if space.is_locked else ""
    lines.append("- (" + space.game_code + ") " + space.room.name + locked_message)
    for interaction in space.interactions:
      lines.append("  - " + interaction.furniture.name)
  add_lines_to_file(lines, id)

def setup_mansion(id):
  print("setting up mansion...")
  setup_spaces(id)
  # TODO each room needs:
  #   furniture
  # TODO each HINT interaction needs
  #   requirement
  #   type
  #   message
