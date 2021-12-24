from tasks.game_file_writer import add_line_to_file, add_lines_to_file
from tasks.info_reader import read_clues, read_assets
import random

def select_person(clues, id):
  people = []
  for clue in clues:
    if clue.get_is_person():
      people.append(clue.name)
  random.shuffle(people)
  lines = [
    "Person #1 - " + people[0] + " : needed for MONEY",
    "Person #2 - " + people[1] + " : needed for PRIVATE HINT #12",
    "Person #3 - " + people[2] + " : needed for PRIVATE HINT #11",
    "Person #4 - " + people[3] + " : needed for PRIVATE HINT #10",
  ]
  add_lines_to_file(lines, id)

def select_item(clues, id):
  items = []
  for clue in clues:
    if clue.get_is_item():
      items.append(clue.name)
  random.shuffle(items)
  lines = [
    "Item #1: " + items[0] + ": needed for MONEY",
    "Item #2: " + items[1] + ": needed for PRIVATE HINT #12",
    "Item #3: " + items[2] + ": needed for PRIVATE HINT #9",
    "Item #4: " + items[3] + ": needed for PRIVATE HINT #8",
  ]
  add_lines_to_file(lines, id)

def shuffle_cards(clues, id):
  clue_deck = []

  for clue in clues:
    clue_deck.append(clue.name)

  random.shuffle(clue_deck)
  add_line_to_file("Clue Deck: " + str(clue_deck), id)

def prepare_clue_deck(id):
  print("preparing clue deck...")
  assets = read_assets()
  
  clues = read_clues()
  random.shuffle(clues)

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
    asset.clue_name = key_clues[index].name

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
    asset.clue_name = people_clues[index].name

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
    asset.clue_name = item_clues[index].name

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
    asset.clue_name = remaining_clues[index].name

  lines = [
    "## Clue Setup",
  ]
  for asset in key_assets + people_assets + item_assets + people_or_item_assets:
    lines.append(" - " + asset.name + " : " + asset.clue_name)

  add_lines_to_file(lines, id)
  
  shuffle_cards(clues, id)
