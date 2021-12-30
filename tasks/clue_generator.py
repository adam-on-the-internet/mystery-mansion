from tasks.style_reader import read_clues, read_assets
import random

def generate_clues(style):
  assets = read_assets(style)
  random.shuffle(assets)
  clues = read_clues(style)

  # assign keys to key assets
  key_clues = []
  for clue in clues:
    if clue.get_is_key():
      key_clues.append(clue)
  key_assets = []
  for asset in assets:
    if asset.get_is_key():
      key_assets.append(asset)
  for index, asset in enumerate(key_assets):
    asset.clue = key_clues[index]

  # assign people to people assets
  people_clues = []
  for clue in clues:
    if clue.get_is_person():
      people_clues.append(clue)
  people_assets = []
  for asset in assets:
    if asset.get_is_person():
      people_assets.append(asset)
  for index, asset in enumerate(people_assets):
    asset.clue = people_clues[index]

  # assign item to item assets
  item_clues = []
  for clue in clues:
    if clue.get_is_item():
      item_clues.append(clue)
  item_assets = []
  for asset in assets:
    if asset.get_is_item():
      item_assets.append(asset)
  for index, asset in enumerate(item_assets):
    asset.clue = item_clues[index]

  # assign remaining clues to remaining assets

  generic_assets = 0 # count assets that use a person OR an item
  for asset in assets:
    if asset.get_is_person_or_item():
      generic_assets = generic_assets + 1
  half_generic_assets = int(generic_assets / 2)
  generic_buffer = -1 * half_generic_assets # -2 for classic/sequel, -1 for small
  
  remaining_people = people_clues[generic_buffer:]
  remaining_items = item_clues[generic_buffer:]
  remaining_clues = remaining_people + remaining_items
  random.shuffle(remaining_clues)
  people_or_item_assets = []
  for asset in assets:
    if asset.get_is_person_or_item():
      people_or_item_assets.append(asset)
  for index, asset in enumerate(people_or_item_assets):
    asset.clue = remaining_clues[index]
  all_assets = key_assets + people_assets + item_assets + people_or_item_assets
  return all_assets
