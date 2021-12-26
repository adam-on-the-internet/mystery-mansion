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

def populate_space_hint(interaction, spaces):
  # TODO populate hint messages properly
  if "_notfurniture_" in interaction.hint:
    interaction.hint = interaction.hint.replace("_notfurniture_", "?")
  elif "_notroom_" in interaction.hint:
    interaction.hint = interaction.hint.replace("_notroom_", "?")
  elif "_moneyroom_" in interaction.hint:
    money_room = get_money_room(spaces)
    interaction.hint = interaction.hint.replace("_moneyroom_", money_room)
  elif "_moneyfurniture_" in interaction.hint:
    money_furniture = get_money_furniture(spaces)
    interaction.hint = interaction.hint.replace("_moneyfurniture_", money_furniture.name)
  print("HINT: " + interaction.hint)

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
