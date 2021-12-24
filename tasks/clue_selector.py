from tasks.game_file_writer import add_line_to_file
from tasks.info_reader import read_clues
import random

def select_person(clues, id):
  people = []
  for clue in clues:
    if clue.get_is_person():
      people.append(clue.name)
  random.shuffle(people)
  selected_person = people[0]
  add_line_to_file("Selected Person: " + selected_person, id)

def select_item(clues, id):
  items = []
  for clue in clues:
    if clue.get_is_item():
      items.append(clue.name)
  random.shuffle(items)
  selected_item = items[0]
  add_line_to_file("Selected Item: " + selected_item, id)

def shuffle_cards(clues, id):
  clue_deck = []

  for clue in clues:
    clue_deck.append(clue.name)

  random.shuffle(clue_deck)
  add_line_to_file("Clue Deck: " + str(clue_deck), id)

def prepare_clue_deck(id):
  print("preparing clue deck...")
  add_line_to_file("## Clue Setup", id)
  clues = read_clues()
  select_person(clues, id)
  select_item(clues, id)
  shuffle_cards(clues, id)
