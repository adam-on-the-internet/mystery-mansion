from tasks.style_reader import read_rooms, read_spaces, read_locked_rooms
from tasks.interaction_generator import generate_interactions
import random
import re

def get_rooms(style):
  rooms = read_rooms(style)
  random.shuffle(rooms)
  return rooms

def get_locked_spaces(spaces, style):
  lockable_spaces = []
  for space in spaces:
    if space.can_be_locked:
      lockable_spaces.append(space.name)
  random.shuffle(lockable_spaces)
  spaces_to_lock = read_locked_rooms(style)
  return lockable_spaces[:spaces_to_lock]  

def populate_requirement(interaction, assets):
  for asset in assets:
    asset_name = asset.name
    clue_name = asset.clue.name
    if asset_name == "Person for Money" and "_personanditemformoney_" in interaction.requirement:
      interaction.required_assets.append(asset)
    elif asset.name == "Item for Money" and "_personanditemformoney_" in interaction.requirement:
      interaction.required_assets.append(asset)
    elif "Person for Hint #" in asset.name and "_personanditemforhint" in interaction.requirement:
      asset_hint_number = get_partial_string('Person for Hint #(.*)', asset.name)
      requirement_hint_number = get_partial_string('_personanditemforhint(.*)_', interaction.requirement)
      if asset_hint_number == requirement_hint_number:
        interaction.required_assets.append(asset)
    elif "Item for Hint #" in asset.name and "_personanditemforhint" in interaction.requirement:
      asset_hint_number = get_partial_string('Item for Hint #(.*)', asset.name)
      requirement_hint_number = get_partial_string('_personanditemforhint(.*)_', interaction.requirement)
      if asset_hint_number == requirement_hint_number:
        interaction.required_assets.append(asset)
    elif "Clue for Hint #" in asset.name and "_personoritemforhint" in interaction.requirement:
      asset_hint_number = get_partial_string('Clue for Hint #(.*)', asset.name)
      requirement_hint_number = get_partial_string('_personoritemforhint(.*)_', interaction.requirement)
      if asset_hint_number == requirement_hint_number:
        interaction.required_assets.append(asset)

    random.shuffle(interaction.required_assets)

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

def get_clue_furniture(spaces, clue_number):
  for space in spaces:
    for interaction in space.interactions:
      if "clue" in interaction.interaction_type:
        if interaction.name.strip() == "Clue #" + str(clue_number):
          return interaction.furniture.name

def get_furniture_count(spaces):
  count = 0
  for space in spaces:
    for interaction in space.interactions:
      count = count + 1
  return count

def get_not_money_furniture(spaces):
  not_money_furniture = []
  money_furniture = get_money_furniture(spaces)
  name = money_furniture.name
  for space in spaces:
    for interaction in space.interactions:
      if name != interaction.furniture.name:
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
      furniture_count_total = get_furniture_count(spaces)
      half_furniture_count = int(furniture_count_total / 2)
      not_money_furniture_selected = not_money_furniture[int(furniture_number) - 1 + (half_furniture_count)]
    interaction.hint = interaction.hint.replace("_notfurniture" + furniture_number + "_", not_money_furniture_selected)
  elif "_clue" in interaction.hint:
    clue_number = get_partial_string('_clue(.*)_', interaction.hint)
    clue_furniture = get_clue_furniture(spaces, clue_number)
    interaction.hint = interaction.hint.replace("_clue" + clue_number + "_", clue_furniture)
  elif "_notroom" in interaction.hint:
    space_number = get_partial_string('_notroom(.*)_', interaction.hint)
    not_money_spaces = get_not_money_spaces(spaces)
    not_money_space = not_money_spaces[int(space_number) - 1]
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

def populate_spaces(interactions, style):
  rooms = get_rooms(style)
  spaces = read_spaces(style)
  locked_spaces = get_locked_spaces(spaces, style)
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

def generate_spaces(assets, style):
  interactions = generate_interactions(style)
  spaces = populate_spaces(interactions, style)
  return populate_messages(spaces, assets)
