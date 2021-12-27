from tasks.game_file_writer import add_lines_to_file
from tasks.info_reader import read_furniture, read_rooms, read_spaces, read_interactions
from tasks.models import MyMansion
import random
import re

def get_clue_interactions(interactions):
  matching_interactions = []
  for interaction in interactions:
    if interaction.has_clue():
      matching_interactions.append(interaction)
  return matching_interactions

def get_non_clue_interactions(interactions):
  matching_interactions = []
  for interaction in interactions:
    if not interaction.has_clue():
      matching_interactions.append(interaction)
  return matching_interactions

def setup_interactions():
  interactions = read_interactions()
  random.shuffle(interactions)

  clue_interactions = get_clue_interactions(interactions)
  non_clue_interactions = get_non_clue_interactions(interactions)
  
  furniture = read_furniture()
  random.shuffle(furniture)

  # We set a max of 1 clue interaction per room.
  # If more than 2 clues are in locked rooms, the game can become unwinnable.
  # Placing 1 clue per room removes that possibility, as only 2 rooms are locked.
  clue_rooms = []
  for interaction in clue_interactions:
    furniture_index = 0
    selected = False
    while not selected:
      selected_furniture = furniture[furniture_index]
      if selected_furniture.selected_room not in clue_rooms:
        clue_rooms.append(selected_furniture.selected_room)
        interaction.furniture = furniture.pop(furniture_index)
        selected = True
      else:
        furniture_index = furniture_index + 1

  # set non-clue interactions
  for index, interaction in enumerate(non_clue_interactions):
    interaction.furniture = furniture[index]

  return clue_interactions + non_clue_interactions  

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
        random.shuffle(space.interactions)
  return spaces

def populate_requirement(interaction, assets):
  # for requirements with person AND item, randomize the order
  if "personanditem" in interaction.requirement:
    requirement_detail = "0"
    if "_personanditemformoney_" in interaction.requirement:
      requirement_detail = "formoney"
    elif "_personanditemforhint12_" in interaction.requirement:
      requirement_detail = "forhint12"
    requirement_order = ["_person#_", "_item#_"]
    random.shuffle(requirement_order)
    first_requirement = requirement_order[0]
    second_requirement = requirement_order[1]
    interaction.requirement = "_x_ and _y_".replace("_x_", first_requirement).replace("_y_", second_requirement)
    interaction.requirement = interaction.requirement.replace("#", requirement_detail, 2)

  # interpolate the clue/asset names
  for asset in assets:
    asset_name = asset.name
    clue_name = asset.clue.name
    if asset_name == "Person for Money":
      interaction.requirement = interaction.requirement.replace("_personformoney_", clue_name)
    elif asset.name == "Item for Money":
      interaction.requirement = interaction.requirement.replace("_itemformoney_", clue_name)
    elif asset.name == "Person for Hint #12":
      interaction.requirement = interaction.requirement.replace("_personforhint12_", clue_name)
    elif asset.name == "Item for Hint #12":
      interaction.requirement = interaction.requirement.replace("_itemforhint12_", clue_name)
    elif asset.name == "Clue for Hint #11":
      interaction.requirement = interaction.requirement.replace("_personoritemforhint11_", clue_name)
    elif asset.name == "Clue for Hint #10":
      interaction.requirement = interaction.requirement.replace("_personoritemforhint10_", clue_name)
    elif asset.name == "Clue for Hint #9":
      interaction.requirement = interaction.requirement.replace("_personoritemforhint9_", clue_name)
    elif asset.name == "Clue for Hint #8":
      interaction.requirement = interaction.requirement.replace("_personoritemforhint8_", clue_name)

def populate_asset_hint(interaction, assets):
  for asset in assets:
    asset_name = asset.name
    clue_name = asset.clue.name
    if asset_name == "Person for Money":
      interaction.hint = interaction.hint.replace("_moneyperson_", clue_name)
    elif asset_name == "Item for Money":
      interaction.hint = interaction.hint.replace("_moneyitem_", clue_name)

def get_money_room(spaces):
  money_furniture = get_money_furniture(spaces)
  return money_furniture.selected_room

def get_money_furniture(spaces):
  for space in spaces:
    for interaction in space.interactions:
      if interaction.has_money():
        return interaction.furniture

def get_not_money_furniture(spaces):
  not_money_furniture = []
  money_furniture = get_money_furniture(spaces).name
  for space in spaces:
    for interaction in space.interactions:
      if money_furniture != interaction.furniture.name:
        not_money_furniture.append(interaction.furniture.name)
  return not_money_furniture

def get_not_money_spaces(spaces):
  not_money_spaces = []
  money_room = get_money_room(spaces)
  for space in spaces:
    room_name = space.room.name
    if room_name != money_room:
      not_money_spaces.append(room_name)
  return not_money_spaces

def get_partial_string(pattern, string):
  result = re.search(pattern, string)
  return result.group(1)

def populate_space_hint(interaction, spaces):
  if "_notfurniture" in interaction.hint:
    furniture_number = get_partial_string('_notfurniture(.*)_', interaction.hint)
    not_money_furniture = get_not_money_furniture(spaces)
    not_money_furniture_selected = not_money_furniture[int(furniture_number) - 1]
    # if the furniture being described is this furniture, select a different furniture
    if interaction.furniture.name == not_money_furniture_selected:
      not_money_furniture_selected = not_money_furniture[int(furniture_number) - 1 + 16]
    interaction.hint = interaction.hint.replace("_notfurniture" + furniture_number + "_", not_money_furniture_selected)
  elif "_notroom" in interaction.hint:
    space_number = get_partial_string('_notroom(.*)_', interaction.hint)
    not_money_spaces = get_not_money_spaces(spaces)
    not_money_space = not_money_spaces[int(space_number)]
    interaction.hint = interaction.hint.replace("_notroom" + space_number + "_", not_money_space)
  elif "_moneyroom_" in interaction.hint:
    money_room = get_money_room(spaces)
    interaction.hint = interaction.hint.replace("_moneyroom_", money_room)
  elif "_moneyfurniture_" in interaction.hint:
    money_furniture = get_money_furniture(spaces)
    interaction.hint = interaction.hint.replace("_moneyfurniture_", money_furniture.name)

def populate_messages(spaces, assets):
  for space in spaces:
    for interaction in space.interactions:
      if interaction.has_hint():
        populate_asset_hint(interaction, assets)
        populate_space_hint(interaction, spaces)
      if interaction.has_requirement():
        populate_requirement(interaction, assets)
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
  return MyMansion(id, assets, spaces)
