from tasks.game_file_writer import add_lines_to_file
from tasks.info_reader import read_furniture, read_rooms, read_spaces, read_interactions
import random

def setup_interactions():
  # TODO one clue in each room MAX
  interactions = read_interactions()
  random.shuffle(interactions)
  furniture = read_furniture()
  for index, interaction in enumerate(interactions):
    interaction.furniture = furniture[index]
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
      space_room = space.room.name.strip().upper()
      interaction_room = interaction.furniture.selected_room.strip().upper()
      if space_room == interaction_room:
        space.interactions.append(interaction)
  return spaces

def populate_messages(spaces, assets):
  for space in spaces:
    for interaction in space.interactions:
      if interaction.has_hint():
        print("HINT: " + interaction.hint)
        # TODO populate hint messages properly
      if interaction.has_requirement():
        # TODO populate requirement messages properly
        print("REQUIREMENT: " + interaction.requirement)
  return spaces

def setup_spaces(assets):
  interactions = setup_interactions()
  spaces = populate_spaces(interactions)
  return populate_messages(spaces, assets)

def describe_spaces(spaces, id):
  lines = ["## Rooms"]
  for space in spaces:
    lines.append("### " + space.to_string())
    for interaction in space.interactions:
      lines.append("- " + interaction.to_string())
  add_lines_to_file(lines, id)  

def setup_mansion(id, assets):
  print("preparing mansion...")
  spaces = setup_spaces(assets)
  describe_spaces(spaces, id)
