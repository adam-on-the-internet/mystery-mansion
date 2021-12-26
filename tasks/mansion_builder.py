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
  return populate_interactions()

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
      space_room = space.room.name.strip().upper()
      interaction_room = interaction.furniture.selected_room.strip().upper()
      if space_room == interaction_room:
        space.interactions.append(interaction)
  return spaces

def setup_spaces(id):
  interactions = setup_interactions(id)
  # TODO one clue in each room MAX

  spaces = populate_spaces(interactions)
  lines = ["## Rooms"]
  for space in spaces:
    lines.append("- " + space.to_string())
    for interaction in space.interactions:
      lines.append("  - " + interaction.to_string())
  add_lines_to_file(lines, id)

def setup_mansion(id):
  print("setting up mansion...")
  setup_spaces(id)
  # TODO each HINT interaction needs
  #   requirement
  #   type
  #   message
