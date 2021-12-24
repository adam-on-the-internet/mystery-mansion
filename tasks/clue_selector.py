from tasks.game_file_writer import add_line_to_file, add_lines_to_file
from tasks.info_reader import read_clues
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
  # TODO use ASSET layer over clues
  add_line_to_file("## Clue Setup", id)
  clues = read_clues()
  select_person(clues, id)
  select_item(clues, id)
  shuffle_cards(clues, id)
