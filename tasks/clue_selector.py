from tasks.game_file_writer import add_line_to_file, add_lines_to_file
from tasks.info_reader import read_clues, read_assets
import random

def describe_assets(assets, id):
  lines = [
    "## Clues",
    "### Setup",
  ]
  for asset in assets:
    lines.append("- " + asset.to_string())
  add_lines_to_file(lines, id)

def describe_clue_deck(clues, id):
  lines = ["### Deck"]
  for clue in clues:
    lines.append("- " + clue.name)
  add_lines_to_file(lines, id)

def shuffle_cards(clues, id):
  random.shuffle(clues)
  describe_clue_deck(clues, id)

def setup_clues(id):
  print("preparing clues...")
  assets = read_assets()
  random.shuffle(assets)
  clues = read_clues()

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
  remaining_people = people_clues[-2:]
  remaining_items = item_clues[-2:]
  remaining_clues = remaining_people + remaining_items
  random.shuffle(remaining_clues)
  people_or_item_assets = []
  for asset in assets:
    if asset.get_is_person_or_item():
      people_or_item_assets.append(asset)
  for index, asset in enumerate(people_or_item_assets):
    asset.clue = remaining_clues[index]
  all_assets = key_assets + people_assets + item_assets + people_or_item_assets
  describe_assets(all_assets, id)
  shuffle_cards(clues, id)
  return all_assets
